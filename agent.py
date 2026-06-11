
from rich import print
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from tools.exporter import Toolkit
from langchain_core.output_parsers import StrOutputParser
from tools.beautiful_soup import scrape
from tools.tavilyapi import web_search



load_dotenv()
toolkit=Toolkit()
tools = toolkit.get_tools()
# llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash"
#                               )

location=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation"
)

llm=ChatHuggingFace(llm=location)
#1agent
def build_search_agent():
    return create_agent(model=llm
                        ,
                        tools=[web_search])

print(tools[1].name)
#2agent
def build_reader_agent():
     return create_agent(model=llm
                        ,
                        tools=[scrape])


writer_prompt=ChatPromptTemplate.from_messages(
     [ ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
          
     ]
     
)
writer_chain=writer_prompt|llm|StrOutputParser()

#critic_prompt

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()

