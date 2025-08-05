from models import get_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

tagging_prompt = ChatPromptTemplate.from_template(
    '''
        Extract the desired information from the following passage. Only extract the properties mentioned in the 
        'Classification' function.

        Passage: {input}
    '''
)

class Classification(BaseModel):
    sentiment: str = Field(default = None, description="The sentiment of the text")
    aggressiveness: str = Field(default = None, description="How aggressiveness is the text from scale 1 to 10")
    language: str = Field(default = None, description="What is the language of the text written in")

structured_output_model = get_model('azure').with_structured_output(Classification)

inp = "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"
prompt = tagging_prompt.invoke({"input": inp})
response = structured_output_model.invoke(prompt)

print(response)

print('Sentiment --> ', response.sentiment) # working