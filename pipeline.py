

from agent import *

from rich import print

def run_research_pipeline(topic:str)->dict:
      state={}
     
     #search agent working
      print("\n"+"="*50)
      print("step 1-search agent is working......")
      print("="*50)

      search_agent=build_search_agent()
      search_result = search_agent.invoke({
        "messages" : [("user",f"Find recent, reliable and detailed information about: {topic}")]
      })
      print("/n search result",search_result)
      state["search_results"]=search_result["messages"][-1].content

      # print("/n search result",state['search_results'])
       #reader agent working
      print("\n"+"="*50)
      print("step 2-reader agent is working......")
      print("="*50)

      reader_agent=build_reader_agent()
      reader_result=reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
      })
      state["scrape_result"]=reader_result["messages"][-1].content
      
      print("/n reader result",state['scrape_result'])
      
      print("\n"+"="*50)
      print("step 3- chain is working......")
      print("="*50)

      research_combined={
            "Search_Result":state['search_results'],
            "Detailed_Scrape_Content":state["scrape_result"]
      }
        
      state["report"]=writer_chain.invoke({"topic":topic,
                          "research":research_combined})

      print('/n print final report',state["report"])

      print("\n"+"="*50)
      print("step 3-critic agent is working......")
      print("="*50)
       
      state["feedback"]=critic_chain.invoke({"report":state['report']})
      print("\n critic report \n", state['feedback'])

      return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)
 


