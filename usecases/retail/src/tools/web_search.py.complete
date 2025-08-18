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
        {"app_id": CONNECTION_TAVILY, "type": ConnectionType.KEY_VALUE}
)
def web_search(query: str) -> str:
    """Use Tavily to search the web and return the top results for a given query string."""

    global tavily_api_key

    if is_called_from_orchestrate == True:
        tavily_api_key = connections.key_value(CONNECTION_TAVILY)['apikey']

    search = TavilySearchResults(max_results=5, tavily_api_key=tavily_api_key)
    results = search.run(query)
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Search string")

    args = parser.parse_args()

    load_dotenv()
    tavily_api_key=os.getenv("TAVILY_API_KEY")
    is_called_from_orchestrate=False

    results = web_search(args.input)
    print("Search results:", results)