# from langchain.schema import HumanMessage, AIMessage

# from backend.services.function_calling.core.models import get_chat_completion

# class ChatHistoryManager:
#     def __init__(self):
#         self.chat_history = []

#     def add_chat(self, question, response):
#         human_message = HumanMessage(content=question)
#         ai_message = AIMessage(content=response)

#         self.chat_history.append(human_message)
#         self.chat_history.append(ai_message)

#         if len(self.chat_history) > 6: self.summarize_history()

#     def summarize_history(self):
#         chat_history = self.to_string()
#         response = get_chat_completion(
#             task = "chat_history",
#             params = {"question": chat_history}
#         )

#         self.reset()
#         self.chat_history.append(
#             HumanMessage(response["question"])
#         )
#         self.chat_history.append(
#             AIMessage(response["response"])
#         )
        

#     def to_string(self):
#         conversation = ""
#         for message in self.chat_history:
#             if isinstance(message, HumanMessage):
#                 conversation += f"User: {message.content}\n"
#             elif isinstance(message, AIMessage):
#                 conversation += f"AI: {message.content}\n"
        
#         return conversation

#     def reset(self):
#         self.chat_history = []

# chat_history_mananger = ChatHistoryManager()