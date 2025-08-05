from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)

chat = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
);

response = chat.invoke("Hello World! How are you?")
print(response.content)