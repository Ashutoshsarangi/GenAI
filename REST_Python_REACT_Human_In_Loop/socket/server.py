
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []
# Dictionary to store pending approval requests
pending_requests = {}

class LLMRequest(BaseModel):
    prompt: str

class ApprovalDecision(BaseModel):
    decision: str
    request_id: str = None


'''
When Socket Open It will be pending state for our communication, 
and now our llm_response will also going for pending state as need user input
'''
@app.websocket("/ws/approval")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast the received message to all connected clients
            print(f"Received from frontend: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)

# Lets call from UI a Separate Button for calling LLM with Prompt

@app.post("/llm-response")
async def llm_response_handler(request: LLMRequest):
    # Generate unique request ID
    request_id = str(uuid.uuid4())
    
    # Create an event to wait for approval decision
    approval_event = asyncio.Event()
    pending_requests[request_id] = {
        "event": approval_event,
        "decision": None,
        "prompt": request.prompt
    }
    
    # Send approval request to frontend via WebSocket
    approval_message = f"Approval needed for prompt: '{request.prompt}'. Request ID: {request_id}"
    for client in clients:
        await client.send_text(approval_message)
    
    # Wait for approval decision (with timeout)
    try:
        await asyncio.wait_for(approval_event.wait(), timeout=300)  # 5 minutes timeout
        
        # Get the decision
        decision = pending_requests[request_id]["decision"]
        
        # Process based on decision
        if decision == "approved":
            # Simulate LLM processing
            llm_response = f"LLM processed your prompt: '{request.prompt}' - Here's the response!"
            status = "completed"
            status_code = 200
        else:
            llm_response = "Request was rejected by human reviewer"
            status = "rejected"
            status_code = 403
            
        # Clean up
        del pending_requests[request_id]
        
        return JSONResponse(
            content={"status": status, "response": llm_response, "request_id": request_id}, 
            status_code=status_code
        )
        
    except asyncio.TimeoutError:
        # Clean up on timeout
        del pending_requests[request_id]
        return JSONResponse(
            content={"status": "timeout", "message": "Approval request timed out"}, 
            status_code=408
        )


@app.post("/approval-decision")
async def approval_decision(decision: ApprovalDecision):
    # Handle approval decision from frontend 
    print(f"Approval decision received: {decision}")
    
    # Find the request by ID (if provided) or use the most recent one
    request_id = decision.request_id
    if not request_id and pending_requests:
        # If no request_id provided, use the most recent request
        request_id = list(pending_requests.keys())[-1]
    
    if request_id in pending_requests:
        # Store the decision and trigger the event
        pending_requests[request_id]["decision"] = decision.decision
        pending_requests[request_id]["event"].set()
        
        return {"status": "decision received", "request_id": request_id}
    else:
        return JSONResponse(
            content={"status": "error", "message": "No pending request found"}, 
            status_code=404
        )


# uvicorn server:app --reload
