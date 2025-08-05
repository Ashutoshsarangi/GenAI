from openai import AzureOpenAI
import json
import requests
import re

azure_endpoint = "https://catalog-openai-gpt4.openai.azure.com/"
api_key = "91e87f01a58f4205a3675c6a782ddcd1" 
api_Version = "2024-05-01-preview"
deployment = "catalog-gpt4-deployment"


client = AzureOpenAI(api_key=api_key, api_version=api_Version, azure_endpoint=azure_endpoint); 

class ChatBot:
    def __init__(self, temprature=0.7, model="gpt-4o", max_tokens=800, frequency_penalty=0, presence_penalty=0):
        self.temprature = temprature
        self.model = model
        self.max_tokens = max_tokens
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        
    
    def ask(self, prompt):
        response = client.chat.completions.create(
            model="catalog-gpt4-deployment",
            messages=[
                {"role": "system", "content": "You are an AI assistant that helps people find information."}, 
                {"role": "user", "content": prompt}
            ],
            temperature=self.temprature,
            max_tokens=self.max_tokens,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )
         # Convert response to dict
        response_dict = response.dict()

        return response_dict['choices'][0]['message']['content']

    
if __name__ == "__main__":
    new_chatbot = ChatBot()
    prompt = f"Extract product offers from the following input: Create a template with Business Internet and business voice. Return the result in the format {{ productOffer: [<list of offers>] }}."
    data = new_chatbot.ask(prompt)
    print(data, data['productOffer']);



# 1. Create a template and add Product offers like Business Internet and BVE
# 2. Create a template and add Business Internet and Data and Voice Equipment (Rental)
# 3. Create a template with product offer Business Internet
# 4. Create a template with Business Internet 
# 4. Create a template with Business Internet and business voice

