
from langchain_core.tools import tool
from models import get_model
from typing import Annotated, TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

@tool
def multiply(a, b):
    '''a * b'''

    return a*b

llm_with_tools = get_model("openai").bind_tools([multiply])

class MessageState(TypedDict):
    message_state: Annotated[list[AnyMessage], add_messages]

#Node
def tool_calling_llm(state):
    return {"message_state": [llm_with_tools.invoke(state["message_state"])]}

#build Graph
graph_builder = StateGraph(MessageState)
graph_builder.add_node("tool_calling_llm", tool_calling_llm)
graph_builder.add_edge(START, "tool_calling_llm")
graph_builder.add_edge("tool_calling_llm", END)

#compile
graph = graph_builder.compile()

#execute

res = graph.invoke({"message_state": "How is the weather"})

print(res)

res1 = graph.invoke({"message_state": "3 multiply by 5"})

print(res1)

