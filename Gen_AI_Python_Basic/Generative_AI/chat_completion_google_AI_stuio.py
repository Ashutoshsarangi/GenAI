from google import genai
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

help(client.models.generate_content)
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="Explain how AI works",
#     stream=True,
#     temperature=0.7,
# )


# #Print stream data
# for chunk in response:
#     print(chunk.text)

