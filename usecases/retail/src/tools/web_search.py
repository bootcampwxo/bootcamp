from ibm_watsonx_orchestrate.agent_builder.tools import ToolPermission, tool
from langchain_community.tools.tavily_search import TavilySearchResults
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.client.connections import ConnectionType
import argparse
import os
from dotenv import load_dotenv

CONNECTION_TAVILY = 'tavily'
tavily_api_key=''
is_called_from_orchestrate=True

@tool(
# insert your code here
)
def web_search(query: str) -> str:

# insert your code here

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Search string")

# insert your code here