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
from cpq_tools import multiply, add, divide, get_product_offers, create_digital_template_prepare_payload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

TOOLS = [multiply, add, divide, get_product_offers, create_digital_template_prepare_payload]
llm_with_tools = get_model("azure").bind_tools(TOOLS)

#System_message
sys_message = SystemMessage(content="You are a helpful assistant tasked with Performaing arithmatic on a set of inputs.")

#Node
def assistant(state):
    return ({"messages": [llm_with_tools.invoke([sys_message] + state["messages"])]})

#Graph 
class State(MessagesState):
    """State for the graph, inheriting from MessagesState."""
    productOfferingInstance: list
    template_payload: dict

graph_builder = StateGraph(State)

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

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserPrompt(BaseModel):
    prompt: str

@app.get("/api/getUserInfo")
def get_user_info():
    return {"message": "get user info sucessfully", "sucess": True}

@app.post("/api/postUserInfo")
async def create_user_info(user_prompt: UserPrompt):
    try:
        print('Request received with prompt:', user_prompt.prompt)  # Debug print
        messages = [HumanMessage(content=user_prompt.prompt)]
        result = react_graph.invoke({"messages": messages})
        
        # Debug prints
        for m in result["messages"][-1:]:
            m.pretty_print()
        
        return {
            "status": "success",
            "payload": result["messages"][-2:][0],
        }
    except Exception as e:
        print('Error:', str(e))  # Debug print
        return {"status": "error", "error": str(e)}

#Working fine

# go to the path and run 
# uvicorn server<File Name>:app --reload
# uvicorn digital_template_mvp_langgraph:app --reload