# CrewAI Minimum Project using Local Models with Ollama
This is a project with the minimum code for CrewAI using Local LLM such as Llama2 via Ollama.

## Ollama using Llama2
https://docs.crewai.com/how-to/LLM-Connections/#using-local-models-with-ollama

```
llm=LLM(model="ollama/llama2", base_url="http://localhost:11434")
```

## Quick Start
### Run Ollama and the local LLM Model
Make sure you have the Prerequisits installed and setup. The local LLM Model, Llama2, should be running on your local machine.

### Run CrewAI application
You can kickoff the application by the following command:
```
Python3 main.py
``` 

## Prerequisits
### Poetry
The libraries are managed by Poetry, so if you have not yet installed it, please install it with the following command:
```
curl -sSL https://install.python-poetry.org | python3 -
```
(note) Reference: https://medium.com/@mronakjain94/comprehensive-guide-to-installing-poetry-on-ubuntu-and-managing-python-projects-949b49ef4f76


## Setup Environment
### Install Dependencies
Run the following command from the project home directory:
```
poetry install
```

### Ollama and Llama2
#### Install Ollama
Follow the instruction provided by the Ollama.com (https://ollama.com/download)

```(e.g. with Ubuntu)
curl -fsSL https://ollama.com/install.sh | sh
```

#### Pull the desired model (e.g. ollama2)
```
ollama pull llama2
```

#### Run the desired model (e.g. ollama2)
```
ollama run llama2
```
You should be able to confirm by accessing http://127.0.0.1:11434/
```(HTTP Response)
Ollama is running
```