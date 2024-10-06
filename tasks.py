from crewai import Task
from textwrap import dedent

class SearchTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def search_a_keyword(self, agent, keyword):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Search a meaning of the keyword
                    **Description**: Analyze and select the best explanation for the given keyword in the area of the Internet and Information Technology areas. The information should be in English only.

                    **Parameters**: 
                    - Keyword: {keyword}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output='The meaning of the keyword in details. The summary should be given first followed by the detailed explanation'
        )
