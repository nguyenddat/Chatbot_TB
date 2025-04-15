from services.chatbot_agents.llm_clients.prompts import procedure_selector
from services.chatbot_agents.llm_clients.clients import get_chat_completion
from services.chatbot_agents.retrievers.procedure_retriever import retriever
from services.chatbot_agents.helpers import procedures

class ProcedureAgent:
    def __init__(self):
        self.description = "Đây là agent được chuyên dụng đối với nhiệm vụ hỏi đáp về một thủ tục cụ thể. Nếu người dùng cần hỏi về thủ tục cụ thể nào đó, agent nên được ưu tiên. Nếu người dùng hỏi chung chung như tôi phù hợp với thủ tục nào, không nên sử dụng agent này."

        self.propmt = procedure_selector.procedure_selector_prompt


    def get_response(self, question, chat_history):
        # Get 10 docs relevant
        docs = retriever.retriever.invoke(
            question,
            config = {"k": 10}
        )
        docs = "\n".join([doc.page_content for doc in docs])
        print(docs)

        # Invoke llm
        response = get_chat_completion(
            task = "procedure",
            params = {
                "procedure_descriptions": docs,
                "question": question,
                "chat_history": chat_history
            }
        )

        if response["function_id"] == "":
            return {"response": response["response"], "recommendations": response["recommendations"]}
        
        thu_tuc_id = response["function_id"]
        thu_tuc_params = response["function_params"]
        thu_tuc_duoc_chon = procedures.get_by_id(id = thu_tuc_id, params = thu_tuc_params)
        response = {
            "response": procedures.to_string(thu_tuc_duoc_chon),
            "recommendations": response["recommendations"]
        }
        return response

procedure_selector = ProcedureAgent()
        

