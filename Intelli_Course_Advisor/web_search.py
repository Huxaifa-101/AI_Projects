from tavily import TavilyClient

# Initialize Tavily client with API key
# You can also set the key as an environment variable instead of hardcoding
client = TavilyClient(api_key="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")

def tavily_search(query: str) -> str:
    """
    Run a web search using Tavily and return formatted results.

    Args:
        query (str): the search query

    Returns:
        str: a string listing titles and URLs of top results, or "No results found."
    """
    # perform the search
    res = client.search(query)

    # extract results list
    results = res.get("results", [])

    # handle empty results
    if not results:
        return "No results found."

    # format results as "Title: URL" per line
    return "\n".join([f"{item['title']}: {item['url']}" for item in results])
