from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from models import get_model

class Person (BaseModel):
    '''Information about a person'''
    name: Optional[str] = Field(default=None, description="The name of the person")
    hair_color: Optional[str] = Field(default=None, description="The hair color of the person, if known")
    height_in_cm: Optional[str] = Field(default=None, description="The height of the person in centimeters, if known")


prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction Algorithm."
            "Only extract relevant information from the text."
            "If you don't have the value of an attribute, asked to extract"
            "return null for the attribute value."
        ),
        ('human', '{text}')
    ]
)


structured_llm_model = get_model('azure').with_structured_output(Person)

text = 'Ashu Sarangi is 6feet tall and red hair'
prompt = prompt_template.invoke({"text": text})

res = structured_llm_model.invoke(prompt)

print(res) # Use one of 'human', 'user', 'ai', 'assistant', or 'system' as role