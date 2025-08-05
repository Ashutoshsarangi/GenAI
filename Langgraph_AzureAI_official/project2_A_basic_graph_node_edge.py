import random
from typing import TypedDict
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    graph_state: str;

def node1(state):
    print("---Node1---")
    return {"graph_state": state["graph_state"] + ' I am '}

def node2(state):
    print('---Node2---')
    return {"graph_state": state["graph_state"] + " Happy!! "}

def node3(state):
    print("---Node3---")
    return {"graph_state": state["graph_state"] + " Sad!! "}

def decide_mood_from_node(state):
    current_state_info = state["graph_state"]

    if random.random() < 0.5:
        return "node_2" #node name
    
    return "node_3" #node_name

#Graph Construction

#build Graph
graph_builder = StateGraph(State)
graph_builder.add_node("node_1", node1)
graph_builder.add_node("node_2", node2)
graph_builder.add_node("node_3", node3)

#Logic

graph_builder.add_edge(START, "node_1")
graph_builder.add_conditional_edges("node_1", decide_mood_from_node)
graph_builder.add_edge("node_2", END)
graph_builder.add_edge("node_3", END)

#Compile

graph = graph_builder.compile()

#view
display(Image(graph.get_graph().draw_mermaid_png()))

#Execute

res = graph.invoke({"graph_state": "hello Ashu here"})

print('Final result ---> ', res)