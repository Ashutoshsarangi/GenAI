from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "User API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "User API"}

@app.get("/api/getUserInfo")
def get_user_info():
    return {"message": "get user info sucessfully", "sucess": True}

@app.post("/api/postUserInfo")
def create_user_info(user: User):
    return {"message": f"Received item: {user.name} with value {user.age}"}


#Working fine

# go to the path and run 
# uvicorn server:app --reload