from typing import Union, Dict
from autogen import ConversableAgent, Agent
from zep_cloud.client import Zep
from zep_cloud import Message, ThreadContextResponse


class ZepConversableAgent(ConversableAgent):  # Agent with Zep memory
    """A custom ConversableAgent that integrates with Zep for long-term memory."""

    def __init__(
        self,
        name: str,
        system_message: str,
        llm_config: dict,
        function_map: dict,
        human_input_mode: str,
        zep_session_id: str,
        zep_client: Zep,
        min_fact_rating: float,
    ):
        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config,
            human_input_mode=human_input_mode,
            function_map=function_map,
        )
        self.zep_session_id = zep_session_id
        self.zep_client = zep_client
        self.min_fact_rating = min_fact_rating
        # Store the original system message as we will update it with relevant facts from Zep
        self.original_system_message = system_message
        self.register_hook(
            "process_message_before_send", self._zep_persist_assistant_messages
        )
        # Note: Persisting user messages needs to happen *before* the agent
        # processes them to fetch relevant facts. We'll handle this outside
        # the hook based on Streamlit input.

    def _zep_persist_assistant_messages(
        self,
        message: Union[Dict, str],
        sender: Agent,
        recipient: Agent,
        silent: bool,
    ):
        """Agent sends a message to the user. Add the message to Zep."""
        if sender == self:
            if isinstance(message, dict):
                content = message.get("content", "")
            else:
                content = str(message)

            if content:
                # Truncate if exceeds Zep's 4096 character limit
                MAX_CONTENT_LENGTH = 4096
                if len(content) > MAX_CONTENT_LENGTH:
                    content = content[:MAX_CONTENT_LENGTH - 50] + "\n\n[Message truncated due to length]"
                
                zep_message = Message(
                    role_type="assistant",
                    role="assistant",
                    content=content,
                    metadata={"agent_name": self.name}
                )
                self.zep_client.thread.add_messages(
                    thread_id=self.zep_session_id, messages=[zep_message]
                )
        return message

    def _zep_fetch_and_update_system_message(self):
        """Fetch facts and update system message."""
        context_response: ThreadContextResponse = self.zep_client.thread.get_user_context(
            thread_id=self.zep_session_id, mode="facts"
        )
        context = context_response.context or "No specific facts recalled."

        # Update the system message for the next inference
        self.update_system_message(
            self.original_system_message
            + f"\n\nRelevant facts about the user and prior conversation:\n{context}"
        )

    def _zep_persist_user_message(self, user_content: str, user_name: str = "User"):
        """User sends a message to the agent. Add the message to Zep."""
        if user_content:
            # Truncate if exceeds Zep's 4096 character limit
            MAX_CONTENT_LENGTH = 4096
            if len(user_content) > MAX_CONTENT_LENGTH:
                user_content = user_content[:MAX_CONTENT_LENGTH - 50] + "\n\n[Message truncated due to length]"
            
            zep_message = Message(
                role_type="user",
                role="user",  # Always use "user" - API requirement
                content=user_content,
                metadata={"user_name": user_name}  # Store actual name in metadata
            )
            self.zep_client.thread.add_messages(
                thread_id=self.zep_session_id, messages=[zep_message]
            )
