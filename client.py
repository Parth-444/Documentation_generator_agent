from langgraph.graph import StateGraph, START
from langchain.tools import tool
from langchain_ollama import ChatOllama
from typing import TypedDict, List
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

llm = ChatOllama(model="llama3:8B")
# response = llm.invoke("what is the full name of hitler, and why was he able to rise in power despite being from a poor family")

# print(response)

async def get_mcp_tools():
    # client = MultiServerMCPClient(
    #     {
    #         "repo_tools": {
    #             "command": "uv",
    #             "args": ["main.py"],
    #             "transport": "stdio"
    #         }
    #     }
    # )
    client = MultiServerMCPClient(
    {
        "github_server": {
            "command": "uv",
            "args": [
                "run",
                "python",
                "C:\\Users\\Parth\\Desktop\\github_mcp_server\\main.py"
            ],
            "transport": "stdio"
        }
    }
)


    tools = await client.get_tools()
    return tools

tools = asyncio.run(get_mcp_tools())
# llm_with_tools = llm.bind_tools(tools)
repo_tree_tool = next(t for t in tools if t.name == "get_repo_tree")



class AgentState(TypedDict):
    messages: str
    repo_name : str | None
    repo_tree: List

async def planner_node(state: AgentState) -> AgentState:
    """Takes the repo name then gets the repo tree from MCP server"""
    repo_tree = await repo_tree_tool.ainvoke({"repo_name": state["repo_name"]})
    state["repo_tree"] = repo_tree
    return state


workflow = StateGraph(AgentState)

workflow.add_node("planner_node", planner_node)
workflow.add_edge(START, "planner_node")



app = workflow.compile()

initial_state = {
    "messages": "",
    "repo_name": "voice_agent",
    "repo_tree": []
}

result = asyncio.run(app.ainvoke(initial_state))
print("Repo Tree: ", result["repo_tree"])