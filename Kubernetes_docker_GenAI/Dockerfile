FROM python:3.9.6-slim

WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install uvicorn fastapi pydantic

# firewall-cmd --permanent --add-port=5000/tcp
# firewall-cmd --reload
# firewall-cmd --state

# Expose port 5000
EXPOSE 9000

# Command to run the application server.py file is inside app folder
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "9000"]


# docker build -t genai-server-poc-ashu:1.8.0 .
# docker run -d -p 8080:9000 --name my-genai-app-ashu genai-server-poc-ashu:1.8.0

# Open your web browser and navigate to http://localhost:8080 (or http://your-host-ip:8080 if accessing from another machine).

# INFO:     Uvicorn running on http://127.0.0.1:9000 (Press CTRL+C to quit)
# This indicates that Uvicorn is binding to 127.0.0.1 (localhost) inside the container. When Uvicorn binds to 127.0.0.1, it means it's only listening for connections originating from within the container itself.

# Your docker run -p 8080:9000 command correctly maps host port 8080 to container port 9000. However, even though port 9000 is open on the container's network interface, Uvicorn isn't listening for external connections on that port because it's specifically bound to localhost.

# The Solution: Tell Uvicorn to Bind to All Interfaces

# You need to instruct Uvicorn to listen on 0.0.0.0 (all available network interfaces) inside the container. This makes it accessible from your host machine via the port mapping.

#  it is sending 9000 and making 8080 available for out side of container i.e out machine browser