'''
1. act:- Let the model call specific tool
2. Observe:- Pass the tool output back to Model
3. Reason- Let the Model reasoning about the tool's output to decide what to do next
    Example:- to call another tool / respond directly
'''

from models import get_model
from langgraph.graph import MessagesState, START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import SystemMessage, HumanMessage


def multiply(a,b):
    '''a*b'''
    return a*b


def add(a,b):
    '''a+b'''
    return a+b

def divide(a,b):
    '''a/b'''
    return a/b

TOOLS = [multiply, add, divide]

llm_with_tools = get_model("azure").bind_tools(TOOLS)

#System_message
sys_message = SystemMessage(content="You are a helpful assistant tasked with Performaing arithmatic on a set of inputs.")

#Node
def assistant(state):
    return ({"messages": [llm_with_tools.invoke([sys_message] + state["messages"])]})

#Graph 

graph_builder = StateGraph(MessagesState)

#Adding Nodes

graph_builder.add_node('assistant', assistant)
graph_builder.add_node('tools', ToolNode(TOOLS))

#define Edges
graph_builder.add_edge(START, 'assistant')
'''
If the latest message from assistant is a tool call --> tools_condition routes to tools
if the latest message from assistant is not a tool call --> tools_condition routes to END
'''
graph_builder.add_conditional_edges('assistant', tools_condition)
graph_builder.add_edge('tools', 'assistant')

react_graph = graph_builder.compile()

messages = [HumanMessage(content="Add 3 and 4. Multiply the output by 3 and then divide by 5")]

messages = react_graph.invoke({"messages": messages})

for m in messages["messages"]:
    m.pretty_print()