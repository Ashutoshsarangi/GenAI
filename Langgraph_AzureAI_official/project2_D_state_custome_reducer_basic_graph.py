from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END

# The reducer function (or update logic) is responsible for adding vs. replacing data.
# The annotation is just a hint or metadata; it does not perform the operation.

def reducer_fun_list(left: list | None, right: list | None) -> list:
    """Custom reducer function to add two lists."""
    if (not left or left is None):
        left = []
    if right is None:
        right = []
    
    return left + right

class State(TypedDict):
    foo: Annotated[list[int], reducer_fun_list]

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
res = graph.invoke({"foo": None}) # This is working fine.

print('Final result ---> ', res)