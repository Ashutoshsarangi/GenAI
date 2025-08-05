from pydantic import BaseModel, Field
from models import get_model
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt.chat_agent_executor import AgentState
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

class WeatherResponse(BaseModel):
    conditions: str = Field(default=None, description = "What is the weather condition")

def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The current weather in {location} is sunny with a temperature of 25°C."

def prompt(state: AgentState, config: RunnableConfig):
    user_name = config["configurable"].get("user_name")
    system_msg = f"You are a helpful assistant. Address the user as {user_name}"

    return [{"role": 'system', "content": system_msg}] + state["messages"]

#Create an agent
azure_model = get_model(provider="azure")

agent = create_react_agent(
    model=azure_model,
    tools=[get_weather],
    prompt=prompt,
    response_format=WeatherResponse,
    checkpointer=checkpointer
)

config = {"configurable": {"user_name": 'Ashutosh Sarangi', "thread_id": "12"}}

# Run the agent with a user prompt
result = agent.invoke({"messages": [{"role": "user", "content": "What is the weather in Limassole?"}]},
                      config = config)

# lets say we want our previous context when we do another invoke we need to send the same config here.
# So it will have the history from first conversation automatically

print(result["structured_response"]) # we need to have structured output.
print(result["structured_response"].conditions) # we need to have structured output.
