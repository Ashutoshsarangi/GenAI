import random
from typing import TypedDict, Literal
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langchain_core.pydantic_v1 import BaseModel, validator

class PydanticState(BaseModel):
    name: str
    mood: Literal["happy", "sad"]

    @validator('mood')
    def validate_mood(cls, value):
        if (value not in ["happy", "sad"]):
            raise ValueError("Mood Should Be One of these happy or sad")
        return value

def node1(state):
    print("---Node1---")
    return {"name": state.name + ' I am '}

def node2(state):
    print('---Node2---')
    return {"name": state.name + " Happy!! "}

def node3(state):
    print("---Node3---")
    return {"name": state.name + " Sad!! "}

def decide_mood_from_node(state):
    current_state_info = state.name

    if random.random() < 0.5:
        return "node_2" #node name
    
    return "node_3" #node_name

#Graph Construction

#build Graph
graph_builder = StateGraph(PydanticState)
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

res = graph.invoke({"name": "Ashu", "mood": "happy"}) # This is working fine.
#res = graph.invoke({"name": "Ashu", "mood": "mda"})# it will through an exception

print('Final result ---> ', res)