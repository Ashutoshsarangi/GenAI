import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import AzureChatOpenAI, ChatOpenAI

load_dotenv(find_dotenv(), override=True)

def get_model(provider="azure"):
    if provider == "azure":
        return AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )
    elif provider == "openai":
        return ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-4o",  # or your preferred model
        )
    else:
        raise ValueError("Unknown provider")