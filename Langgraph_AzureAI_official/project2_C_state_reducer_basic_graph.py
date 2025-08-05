import random
import operator
from typing import TypedDict, Literal, Annotated
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

# The reducer function (or update logic) is responsible for adding vs. replacing data.
# The annotation is just a hint or metadata; it does not perform the operation.

class State(TypedDict):
    foo: Annotated[list[int], operator.add]

def node_1(state):
    print("---Node1---")
    return {"foo": [state["foo"][0] + 1]}


#Graph Construction

#build Graph
graph_builder = StateGraph(State)
graph_builder.add_node("node_1", node_1)

#Logic

graph_builder.add_edge(START, "node_1")
graph_builder.add_edge("node_1", END)

#Compile

graph = graph_builder.compile()

#Execute
res = graph.invoke({"foo": [2]}) # This is working fine.

print('Final result ---> ', res)