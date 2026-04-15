from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

class TavilySearch:
    def __init__(self):
        self.client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def search(self, query, k=3):
        try:
            response = self.client.search(
                query=query,
                search_depth="advanced",
                max_results=k
            )

            results = []
            for r in response.get("results", []):
                results.append({
                    "content": r.get("content", ""),
                    "source": r.get("url", "")
                })

            return results

        except Exception as e:
            print("Tavily error:", e)
            return []