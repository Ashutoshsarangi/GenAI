from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

TOOLS = [get_weather, multiply]