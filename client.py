from langgraph.graph import StateGraph, START
from langchain.tools import tool
from langchain_ollama import ChatOllama
from typing import TypedDict, List
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import json
import yaml

with open("prompts/file_selector.yaml") as f:
    p = yaml.safe_load(f)

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
list_repos_tool = next(t for t in tools if t.name == "list_repos")



class AgentState(TypedDict):
    messages: str
    repo_name : str | None
    repo_tree: List
    important_files : List

async def planner_node(state: AgentState) -> AgentState:
    """Takes the repo name then gets the repo tree from MCP server"""
#     list_all_repos = await list_repos_tool.ainvoke({})
    
#     fuzzy_match = await llm.ainvoke(f"""You are given a list of GitHub repository names: {list_all_repos}
# The user provided this repo name: {state['repo_name']}

# Your task is to find the single best matching repository name from the list.

# Match based on:

# semantic similarity

# partial words

# hyphens vs spaces

# abbreviations

# casing differences

# Return only the exact repository name from the list.
# If no reasonable match exists, return "NOT_FOUND".

# Do not explain your reasoning. Output only the repo name.""")
    
    # resolved_repo = fuzzy_match.content.strip()
    # state["repo_name"] = resolved_repo

    repo_tree = await repo_tree_tool.ainvoke({"repo_name": state["repo_name"]})
    state["repo_tree"] = repo_tree
    return state

async def structure_analyzer_node(state: AgentState) -> AgentState:
    """Takes repo structure from the planner node then analyzes which files are important to read for the documentation"""

    system_prompt = p["system"]
    user_prompt = p["user"].format(project_tree=state["repo_tree"])

    prompt = system_prompt + user_prompt
    raw = (await llm.ainvoke(prompt)).content

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        fix_prompt = f"Fix this to valid JSON ONLY:\n{raw}"
        raw = (await llm.ainvoke(fix_prompt)).content
        parsed = json.loads(raw)

    state["important_files"] = parsed
    return state
    

workflow = StateGraph(AgentState)

workflow.add_node("planner_node", planner_node)
workflow.add_node("structure_analyzer_node", structure_analyzer_node)

workflow.add_edge(START, "planner_node")
workflow.add_edge("planner_node", 'structure_analyzer_node')



app = workflow.compile()

initial_state = {
    "messages": "",
    "repo_name": "emotion-detection",
    "repo_tree": [],
    "important_files": []
}

result = asyncio.run(app.ainvoke(initial_state))
print("important files ", result["important_files"])
