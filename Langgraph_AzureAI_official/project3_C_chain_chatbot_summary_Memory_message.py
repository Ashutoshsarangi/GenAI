from models import get_model
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import SystemMessage, HumanMessage, RemoveMessage
from langgraph.checkpoint.memory import MemorySaver

llm = get_model('azure')

# state["messages"][-2:] will return the last 2 elements from the messages list.

# If there are 2 or more elements, it returns the last 2.
# If there is only 1 element, it returns a list with that 1 element.
# If the list is empty, it returns an empty list.

class State(MessagesState):
    """State for the graph, inheriting from MessagesState."""
    summary: str

def call_modal(state: State):
    summary = state.get("summary", "")

    if summary:
        # Add summary to system Message
        messages = [SystemMessage(content=f"Summarize the following conversation: {summary}")] + state["messages"]
    else:
        # If no summary, just use the messages
        messages = state['messages']
    
    response = llm.invoke(messages)
    return {"messages": response}

# Define node to produce Summary

def summarize_conversation(state: State):
    summary = state.get("summary", "")

    if summary:
        summary_message = (f"This is summary of the conversation: {summary}\n\n"
                           "extend the summary by taking into account the new message above:")
    else:
        summary_message = "create summary of the conversation above:"
    
    messages = state['messages'] + [HumanMessage(content=summary_message)]
    response = llm.invoke(messages)

    # Delete all but the 2 most recent messages
    delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:-2]]#state['messages'][:-2] if len(state['messages']) > 2 else state['messages']
    return {"summary": response.content, "messages": delete_messages}

def should_continue(state: State):
    #"return the next node to execute"

    messages = state["messages"]
    if len(messages) > 6:
        return "summarize_conversation"
    
    return END



#build Graph
graph_builder = StateGraph(State)
graph_builder.add_node("conversation", call_modal)
graph_builder.add_node(summarize_conversation)

graph_builder.add_edge(START, "conversation")
graph_builder.add_conditional_edges("conversation", should_continue)
graph_builder.add_edge("summarize_conversation", END)

#compile
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

#create a thread
config = {"configurable": {"thread_id": "1"}}

#Start Conversation
res = graph.invoke({"messages": [HumanMessage(content="Hello, I am Ashutosh.")]}, config)
for m in res["messages"][-1:]:
    m.pretty_print()

res = graph.invoke({"messages": [HumanMessage(content="What is my name.")]}, config)
for m in res["messages"][-1:]:
    m.pretty_print()

