from models import get_model
from langgraph.graph.message import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import trim_messages # this is another option to trim messages

llm = get_model('azure')

# state["messages"][-2:] will return the last 2 elements from the messages list.

# If there are 2 or more elements, it returns the last 2.
# If there is only 1 element, it returns a list with that 1 element.
# If the list is empty, it returns an empty list.


#Node
def tool_calling_llm(state):
    return {"message_state": [llm.invoke(state["messages"][-2:])]} # last 2 messages, rather than sending all the messages to the LLM

#build Graph
graph_builder = StateGraph(MessagesState)
graph_builder.add_node("tool_calling_llm", tool_calling_llm)
graph_builder.add_edge(START, "tool_calling_llm")
graph_builder.add_edge("tool_calling_llm", END)

#compile
graph = graph_builder.compile()

#execute

res = graph.invoke({"message_state": "How is the weather"})

print(res)



# There is an also option for trim message from langchain core
