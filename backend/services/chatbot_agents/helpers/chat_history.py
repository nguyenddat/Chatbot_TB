from langchain.schema import HumanMessage, AIMessage
from typing import List, Dict

from backend.services.chatbot_agents.llm_clients.clients import get_chat_completion


class ChatHistoryManager:
    def __init__(self):
        self.chat_history = []

    # def summarize_history(self):
    #     chat_history = self.to_string()
    #     response, tokens = get_chat_completion(
    #         task="chat_history", params={"question": chat_history}
    #     )

    #     self.reset()
    #     self.chat_history.append(HumanMessage(response["question"]))
    #     self.chat_history.append(AIMessage(response["response"]))

    #     print(f"Chat history: {tokens} tokens")

    def _format_chat_history(self, chat_history: List[Dict[str, str]]) -> List:
        converted_chat_history = []
        for message in chat_history:
            if message.get("human") is not None:
                converted_chat_history.append(HumanMessage(content=message["human"]))
            if message.get("ai") is not None:
                converted_chat_history.append(AIMessage(content=""))

        return converted_chat_history

    def to_string(self):
        conversation = ""
        for message in self.chat_history:
            if isinstance(message, HumanMessage):
                conversation += f"User: {message.content}\n"

        return conversation

    def reset(self):
        self.chat_history = []


chat_history_mananger = ChatHistoryManager()
