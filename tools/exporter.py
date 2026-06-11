from tools.tavilyapi import web_search
from tools.beautiful_soup import scrape

class Toolkit:
    def get_tools(self):
        return [scrape, web_search]