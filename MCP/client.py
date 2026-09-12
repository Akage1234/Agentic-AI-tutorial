from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import asyncio

from dotenv import load_dotenv
load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command":"python",
                "args":["MathServer.py"], # ensure correct absolute path
                "transport": "stdio"
            }, 
            "weather": {
                "url":"http://localhost:8000/mcp", # ensure server is running here
                "transport": "streamable_http"
            }
        }
    )

    import os
    tools = await client.get_tools()
    model = init_chat_model(model="google_genai:gemini-flash-lite-latest")
    agent = create_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        {"messages":[{"role":"user", "content": "What is (3 x 5) + 12?"}]}
    )

    print("math_response: ", math_response["messages"][-1].text)

    weather_response = await agent.ainvoke(
            {"messages":[{"role":"user", "content": "what is the weather in california?"}]}
        )
    
    print("weather_response: ", weather_response["messages"][-1].text)

asyncio.run(main())