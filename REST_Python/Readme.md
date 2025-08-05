uvicorn: This is the command to run the Uvicorn server, which is an ASGI server for running FastAPI (and other ASGI apps).
server:app:
server is the name of your Python file (without .py).
app is the FastAPI application instance inside that file.
So, Uvicorn will look for app = FastAPI() inside server.py.
--reload: This option makes the server automatically restart whenever you change your code. It’s useful for development


## Command
uvicorn server:app --reload