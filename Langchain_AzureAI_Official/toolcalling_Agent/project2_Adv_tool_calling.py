import sys
sys.path.append('/Users/sarangia/Desktop/Master/Learning/Gen AI')
from Langchain_AzureAI_Official.models import get_model
from tools import TOOLS
from langchain.agents import initialize_agent, AgentType

LLM_model1 = get_model(provider="azure")
LLM_model2 = get_model(provider="azure") # we can use different model

agent = initialize_agent(
    tools=TOOLS,
    llm=LLM_model1,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

def tool_chain(user_prompt):
     # Step 1: Use agent to get the intermediate answer (calls tools as needed)
    intermediate_result = agent.run(user_prompt)
    
    # Step 2: Use second LLM to refine the answer
    refined_prompt = f"Refine and explain this answer for the user: {intermediate_result}"
    final_result = LLM_model2.invoke(refined_prompt)
    return final_result

result = tool_chain("Multiply 20 with current temperature of Limassole")
print(result)
print(result.content)