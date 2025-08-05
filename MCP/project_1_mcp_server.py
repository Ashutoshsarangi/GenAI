from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP
import json

# Create MCP server instance
mcp = FastMCP("Mathematical Calculator Server")

accounts = {
    "12345": {"balance": 1000.0, "name": "Alice", "transactions": []},
    "67890": {"balance": 500.0, "name": "Bob", "transactions": []}
}

# Register MCP tools
@mcp.tool()
def add_numbers(numbers: List[float]):
    """Add a list of numbers together"""
    result = sum(numbers)
    
    return {"result": result}

@mcp.tool()
def multiply_numbers(numbers: List[float]) -> Dict[str, Any]:
    """Multiply a list of numbers together"""
    result = 1
    for num in numbers:
        result *= num

    return {"result": result}

@mcp.tool()
def divide_numbers(a: float, b: float) -> Dict[str, Any]:
    """Divide two numbers (a / b)"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return {"result": result}

# Define resources
@mcp.resource("greeting://{name}/{age}")
def get_greeting(name: str, age: str) -> str:
    """Get a personalized greeting for a user"""
    return f"Hello {name}, {age}, welcome to the Mathematical Calculator Server!"

@mcp.resource("get://users")
def get_users() -> str:
    """Get list of registered users"""
    return json.dumps({"users": {"name": "Ashutosh Sarangi"}}, indent=2)

@mcp.resource("account://{account_id}/statement")
def get_account_statement(account_id: str) -> str:
    """Get account statement (RESOURCE - read-only data)"""
    if account_id not in accounts:
        return json.dumps({"error": "Account not found"})
    
    account = accounts[account_id]
    statement = {
        "account_id": account_id,
        "account_holder": account["name"],
        "current_balance": account["balance"],
        "transactions": account["transactions"],
    }
    return json.dumps(statement, indent=2)

@mcp.resource("bank://branch/{branch_id}/info")
def get_branch_info(branch_id: str) -> str:
    """Get bank branch information (RESOURCE - static data)"""
    branches = {
        "001": {"name": "Main Branch", "address": "123 Main St", "phone": "555-0001"},
        "002": {"name": "Downtown", "address": "456 Oak Ave", "phone": "555-0002"}
    }
    return json.dumps(branches.get(branch_id, {"error": "Branch not found"}), indent=2)

@mcp.resource("bank://rates")
def get_interest_rates() -> str:
    """Get current interest rates (RESOURCE - configuration data)"""
    rates = {
        "savings": 2.5,
        "checking": 0.1,
        "loan": 5.25,
        "mortgage": 3.75,
        "last_updated": "2025-01-31"
    }
    return json.dumps(rates, indent=2)

if __name__ == "__main__":
    # Run the MCP server with http transport
    # mcp.run(transport="http", host="localhost", port=5000)
    import uvicorn
    # Run the MCP server with uvicorn
    uvicorn.run(mcp.app, host="localhost", port=5000, log_level="info")