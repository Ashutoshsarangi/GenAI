from models import get_model
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

model = get_model("azure")

# messages = [
#     SystemMessage("Translate the following text to French:"),
#     HumanMessage("Hello, how are you?"),
# ]

system_template = 'Translate the following text to {language}:'
user_template = '{text}'
prompt_template = ChatPromptTemplate([('system', system_template), ('user', user_template)])

prompt = prompt_template.invoke({"language": "French", "text": "Hello, how are you, Ashutosh?"})

print('Prompt:', prompt)  # This will print the prompt that will be sent to the model
res = model.invoke(prompt)

print(res.content)  # This will print the translated text