'''
Tools are a way to encapsulate a function and its schema in a way that can be passed to a chat model.
Create tools using the @tool decorator, which simplifies the process of tool creation, supporting the following:
    Automatically infer the tool's name, description and expected arguments, while also supporting customization.
    Defining tools that return artifacts (e.g. images, dataframes, etc.)
    Hiding input arguments from the schema (and hence from the model) using injected tool arguments.

NOTE:- 
Earlier I was using bind_tool and invoking the tool but not giving me result, Now I added agents to call my tools Thanks to chatGpt

1. bind_tools only attaches tool schemas to the model, so the LLM can suggest tool calls in its output (it returns a tool call request, not the result).
2. The agent actually manages the full tool-calling loop:
    a. It detects when the LLM wants to call a tool.
    b. It executes the corresponding Python function.
    c. It feeds the tool's result back to the LLM for a final answer.
'''