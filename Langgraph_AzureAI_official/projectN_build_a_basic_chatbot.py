import json
from typing import Annotated
from typing_extensions import TypedDict
from models import get_model
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import ToolMessage
from langgraph.graph.message import add_messages
from langchain_tavily import TavilySearch

'''
1. message key has the type list and add_message function
2. Annotated: defined how this state key should be updated, here it will append messages to the list, rather than
overwriting it.
3. Main key player is the reducer function add_messages, which is used to along with Annotated syntax.
'''
tool = TavilySearch(max_results=2)

# we will add 2 more existing tools once we completed the integration of this TavilySearch
tools = [tool]

class BasicToolNode:
    """"A Node that runs the tool requested in last AIMessage"""
    def __init__(self, tool):
        self.tool_by_name = {tool.name: tool for tool in tools}

    def __call__(self, inputs: dict):
        if messages := inputs.get("messages", []):
            message = messages[-1:]  # Get the last message only
        else :
            print("Error: No messages found in inputs.")
            raise ValueError("No messages found in inputs.")
        print('Message:', message)
        outputs = []
        for tool_call in message.tool_calls:
            tool_result = self.tool_by_name.get(tool_call.name).invoke(tool_call.args)
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call.name,
                    tool_call_id=tool_call.id,
                )
            )
        return {"messages": outputs}
    

class State(TypedDict):
    messages: Annotated[list, add_messages]

llm_model = get_model('azure')
llm_with_tools = llm_model.bind(tools)
graph_builder = StateGraph(State)

#. Add A Node,

'''
It represents units of work and typically regular functions

Notice:-
1. how the chatbot node function takes the current State as input and returns a dictionary containing 
    an updated messages list under the key "messages". 
2. This is the basic pattern for all LangGraph node functions.
3. The add_messages function in our State will append the LLM's response messages to whatever 
    messages are already in the state.
'''

def chatbot(state: State):
    return {"messages": [llm_model.invoke(state["messages"])]}


'''
1st argument is the unique name of the node Name
2nd argumanr is the function that will be executed when the node is called.
'''
graph_builder.add_node("chatbot", chatbot)

tool_node = BasicToolNode(tools)
graph_builder.add_node("tools", tool_node)

# Add Entry Point
graph_builder.add_edge(START, "chatbot")
# Add Exit Point
graph_builder.add_edge("chatbot", END)

# Compile the Graph
graph = graph_builder.compile()


def stream_graph_updated(user_input:str):
    for event in graph.stream(
        {"messages": [{"role": "user", "content": user_input}]}
    ):
        for value in event.values():
            print("Assistant:", value['messages'][-1].content)

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        stream_graph_updated(user_input)
    except KeyboardInterrupt:
        print("\nError Happened, Exiting the chatbot. Goodbye!")
        break

