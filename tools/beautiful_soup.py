import requests
from bs4 import BeautifulSoup

from langchain.tools import tool
from sqlalchemy import true

@tool
def scrape(url:str)->str:
                    """ this scrape the website url provided"""

                            # 1. Download the webpage
                    print("this is url ",url)
                    response = requests.get(url)

                    # 2. Parse the HTML content
                    soup = BeautifulSoup(response.text, "html.parser")
                    for tag in soup(["script","style","nav","footer"]):
                            tag.decompose()

                    # 3. Extract data (e.g., all article titles)
                    return soup.get_text(separator=" ",strip=true)[:300]

# print(scrape.invoke("https://news.ycombinator.com/"))
