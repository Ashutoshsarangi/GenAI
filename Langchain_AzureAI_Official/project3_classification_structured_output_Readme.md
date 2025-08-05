
with_structured_output (e.g., Model.with_structured_output) is used in frameworks like LangChain to instruct the language model to return its output in a structured format, such as a Pydantic model or a specific schema, instead of plain text.

Why use it?

Ensures the model’s output matches a defined structure (e.g., a dictionary, list, or custom object).
Makes it easier to parse, validate, and use the model’s response in your code.
Reduces errors from ambiguous or free-form text output.

from pydantic import BaseModel

class WeatherResult(BaseModel):
    location: str
    temperature: float
    condition: str

structured_model = model.with_structured_output(WeatherResult)
result = structured_model.invoke("What is the weather in Paris?")
print(result.location, result.temperature, result.condition)


