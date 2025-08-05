from langchain_openai import AzureOpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)

def get_embedding_by_model(provider = 'azure'):
    if provider == 'azure':
        # This is not working as we are using gpt-4o model which does not support embeddings
        return AzureOpenAIEmbeddings(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )
    elif provider == 'openai':
        return OpenAIEmbeddings(model="text-embedding-3-large")
    else:
        print('Unknown provider')
        return None
    
if __name__ == '__main__':
    print('I am inside embading_model')
    # This if block will only execute if the script is run directly, 
    #  not if it is imported as a module.