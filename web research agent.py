from tavily import TavilyClient

search_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

from autogen_core.tools import FunctionTool
from typing_extensions import Annotated

async def search_results(search_query : Annotated[str, "A search query to browse the web."], max_results : int = 2) -> str:
    # Perform the search
    results = search_client.search(search_query, max_results=max_results)

    # Format the result
    formatted_results = []
    for result in results["results"]:
        formatted_results.append(
            f"Title: {result["title"]}\nUrl: {result["url"]}\nContent: {result["content"]}\n"
        )
    return f"{10*'-'}\n".join(formatted_results)

# Create the tool.
search_tool = FunctionTool(search_results, description="Search the web.")
