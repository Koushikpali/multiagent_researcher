from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool
load_dotenv()
from rich import print
@tool
def web_search(query:str)->str:
                    """search the web for recent and reliable information """
                    query=query or "who is immuael kant" 
                    client=TavilyClient()
                    response = client.search(
                    query=query,
                    search_depth="advanced",
                    max_results=5
                    )
                    return extractresult(response)
                    # print(response)
                    # print(type(response))

def extractresult(query:dict)->str:
        contents=[]
        for i in query["results"]:
                url = i["url"]
                title = i["title"]
                content = i["content"]
                contents.append(f"Title: {title}\n URL: {url}\n Snippet: {content[:300]}\n")
        return contents



# print(web_search.invoke("blackhole"))
             

