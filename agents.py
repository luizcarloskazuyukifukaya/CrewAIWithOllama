from crewai import Agent
from crewai import LLM

from textwrap import dedent

# from langchain_openai import ChatOpenAI

class SearchAgents:
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(
        #     model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # LOCAL OLLAMA with LLAMA2
        # [install command] ollama pull llama2
        # https://docs.crewai.com/how-to/LLM-Connections/#supported-providers
        self.Ollama = LLM(
            model="ollama/llama2", 
            base_url="http://localhost:11434")

    def search_expert(self):
        return Agent(
            role="Search Keyword Expert",
            backstory=dedent(
                f"""Expert in searching the most detailed information about the given keyword"""),
            goal=dedent(
                f"""Get the most detailed explanation about the meaning of the keyword in the context of Internet and IT related areas"""),
            verbose=True,
            # llm=self.OpenAIGPT4,
            # llm=self.OpenAIGPT35,
            llm=self.Ollama,
        )
