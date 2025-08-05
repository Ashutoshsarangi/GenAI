from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from models import get_model


@tool
def multiply(a, b):
    '''a*b'''

    return a*b

llm = get_model('azure')
llm_with_tools = llm.bind([multiply])

# Here we are using prebuild ToolNode and tool_condition