from crewai import Crew
from textwrap import dedent
from agents import SearchAgents
from tasks import SearchTasks

# This is to load the information from .env
from dotenv import load_dotenv
import os
load_dotenv()  # This loads the variables from .env

# SearchCrew is initialized with the "keyword"
class SearchCrew:
    def __init__(self, keyword):
        self.keyword = keyword

    def run(self):
        # print(f" -- SearchCrew.run() called ")
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = SearchAgents() # defined in agents.py
        tasks = SearchTasks()   # defined in tasks.py

        # Define your custom agents and tasks here
        search_expert = agents.search_expert()

        # Custom tasks include agent name and variables as input
        search_a_keyword = tasks.search_a_keyword(
            search_expert,
            self.keyword,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                search_expert,
            ],
            tasks=[
                search_a_keyword,
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Search Crew")
    print('-------------------------------')

    # Request input from user via command prompt
    keyword = input(
        dedent("""
      What keyword would like to search for?
    """))

    # Create the crew ("SearchCrew from CrewAI") with the keyword given
    search_crew = SearchCrew(keyword)
    # Perform the search asking the crew (search_crew)
    result = search_crew.run()
    # Print the result in the terminal
    print("\n\n################################################")
    print(f"## Here is the result of the search for [{keyword}]")
    print("################################################\n")
    print(result)
