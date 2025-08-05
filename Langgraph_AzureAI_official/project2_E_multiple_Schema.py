from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class InputState(TypedDict):
    question: str

class OutputState(TypedDict):
    answer: str

class OverallState(TypedDict):
    question: str
    answer: str
    notes: str

def thinking_node(state: InputState):
    return {"answer": "bye", "notes": "his name is Ashutosh"}

def answer_node(state: OutputState):
    return {"answer": "bye Ashutosh"}

graph_builder = StateGraph(OverallState, input_schema=InputState, output_schema=OutputState)
graph_builder.add_node("thinking_node", thinking_node)
graph_builder.add_node("answer_node", answer_node)

graph_builder.add_edge(START, 'thinking_node')
graph_builder.add_edge("thinking_node", "answer_node")
graph_builder.add_edge('answer_node', END)

graph = graph_builder.compile()

res = graph.invoke({"question": "What is your name"})

print(res)