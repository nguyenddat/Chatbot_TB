from backend.services.chatbot_agents.llm_clients.prompts import procedure_selector
from backend.services.chatbot_agents.llm_clients.clients import get_chat_completion
from backend.services.chatbot_agents.retrievers.procedure_retriever import retriever
from backend.services.chatbot_agents.helpers import procedures


class ProcedureAgent:
    def __init__(self):
        self.propmt = procedure_selector.procedure_selector_prompt

    def get_response(self, procedure, procedure_params):
        # Get 10 docs relevant
        docs = retriever.retriever.invoke(procedure, config={"k": 5})
        docs = "\n".join([doc.page_content for doc in docs])

        # Invoke llm
        response, tokens = get_chat_completion(
            task="procedure",
            params={
                "procedure_descriptions": docs,
                "question": procedure,
            },
        )

        print("context docs", docs)

        print("response get procedure ID", response)

        if response["procedure_id"] == "":
            return {
                "response": response["response"],
                "recommendations": response["recommendations"],
            }

        thu_tuc_id = response["procedure_id"]
        thu_tuc_duoc_chon = procedures.get_by_id(id=thu_tuc_id, params=procedure_params)
        response = {
            "response": procedures.to_string(thu_tuc_duoc_chon),
            "recommendations": response["recommendations"],
        }
        return response, tokens


procedure_selector = ProcedureAgent()
