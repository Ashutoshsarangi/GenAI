"""
MCP Client for testing the Mathematical Calculator Server
This script helps you inspect and test your MCP server locally
"""

import asyncio
from importlib import resources
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def test_mcp_server():
    """Test the MCP server by calling its tools and resources"""
    
    # Server parameters - pointing to your MCP server script
    server_params = StdioServerParameters(
        command="python3",
        args=["/Users/sarangia/Desktop/Master/Learning/Gen AI/MCP/project_1_mcp_server.py"]
    )
    
    print("🚀 Starting MCP Client Test Session...")
    print("=" * 50)
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            print("✅ Successfully connected to MCP server!")
            
            # List available tools
            print("📋 Available Tools:")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"  • {tool.name}: {tool.description}")
            print()
            
            # List available resources
            print("📋 Available Resources:")
            resources = await session.list_resources()
            print(f"Total resources found: {len(resources.resources)}")
            # only we are going to see the empty resources
            for resource in resources.resources:
                print(f"  • {resource.uri}: {resource.name}")
            print()
            
            # Test addition tool
            print("🧮 Testing Addition Tool:")
            try:
                result = await session.call_tool("add_numbers", {"numbers": [10, 20, 30, 5]})
                print(result)
                print(f"  Result: {json.dumps(result.content[0].text, indent=2)}")
            except Exception as e:
                print(f"  Error: {e}")
            
            # Test greeting resource
            print("👋 Testing Greeting Resource:")
            try:
                result = await session.read_resource("greeting://Ashu/23")
                # print(result)
                print(f"  Result: {result.contents[0].text}")
            except Exception as e:
                print(f"  Error: {e}")
            
            print("🎉 MCP Server testing completed!")


if __name__ == "__main__":
    # Run the async test function
    asyncio.run(test_mcp_server())
