
import sys
sys.path.append('/Users/sarangia/Desktop/Master/Learning/Gen AI')
from Langchain_AzureAI_Official.models import get_model
from tools import TOOLS
from langchain.agents import initialize_agent, AgentType

model = get_model(provider="azure")  # or "openai"
agent = initialize_agent(
    tools=TOOLS,
    llm=model,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# Now, when you run this, the agent will actually call your tool!
result = agent.run("What is the weather in New York?")
print(result)

result_without_tool = agent.run('Hello World!')
print(result_without_tool)

multiply_result = agent.run("What is 5 multiplied 6?")
print(multiply_result)  # This will print the result of the multiplication

multiply_result_new = agent.run("What is 5 times 6?")
print(multiply_result_new)  # This will print the result of the multiplication
