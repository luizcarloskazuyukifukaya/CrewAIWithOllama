# CrewAI Minimum Project using Local Models with Ollama
This is a project with the minimum code for CrewAI using Local LLM such as Llama2 via Ollama.

## Quick Start
### Run Ollama and the local LLM Model
Make sure you have the Prerequisits installed and setup. The local LLM Model, Llama2, should be running on your local machine.

### Run CrewAI application
You can kickoff the application by the following command:
```
Python3 main.py
``` 

## Prerequisites
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

## Ollama using Llama2
The LLM model instance is created using LLM (crewai library), and the model and base_url parameters should be specified accordingly.
(note) Reference: https://docs.crewai.com/how-to/LLM-Connections/#using-local-models-with-ollama

The following is the example for Llama2:
```
from crewai import LLM

...

llm=LLM(model="ollama/llama2", base_url="http://localhost:11434")
```

## Application Example
This is how the application should be like when it is running correctly:
```
kfukaya@kfukaya:~/projects/ai/CrewAIWithOllama$ python3 main.py
## Welcome to Search Crew
-------------------------------

What keyword would like to search for?
Bitcoin
# Agent: Search Keyword Expert
## Task:
**Task**:  Search a meaning of the keyword
**Description**: Analyze and select the best explanation for the given keyword in the area of the Internet and Information Technology areas. The information should be in English only.

**Parameters**:
- Keyword: Bitcoin

**Note**: If you do your BEST WORK, I'll give you a $10,000 commission!

# Agent: Search Keyword Expert
## Final Answer:
Summary: Bitcoin is a decentralized digital currency that allows for peer-to-peer transactions without the need for intermediaries like banks. It was created in 2009 by an anonymous individual or group using the pseudonym Satoshi Nakamoto.

Detailed Explanation:

Bitcoin is a decentralized digital currency that operates on a blockchain, a public ledger that records all transactions. The network is decentralized, meaning there is no central authority controlling it. Transactions are verified by network nodes through cryptographic algorithms, and once confirmed, the transactions are added to the blockchain.

The Bitcoin protocol allows for peer-to-peer transactions without the need for intermediaries like banks. Users can generate their own bitcoins through a process called mining, where they solve complex mathematical problems to validate transactions and add them to the blockchain. Once generated, bitcoins can be transferred between users using specialized software or hardware.

Bitcoin's decentralized nature and use of cryptography make it a secure form of currency. The blockchain technology that underlies Bitcoin provides a tamper-proof record of all transactions, ensuring that the integrity of the network is maintained.

The lack of central control also makes Bitcoin immune to government manipulation or censorship. Transactions are pseudonymous, allowing users to maintain their privacy and avoid government tracking.

Bitcoin's decentralized nature has led to its adoption in various industries, such as finance, gaming, and e-commerce. It has also sparked the development of other cryptocurrencies, such as Ethereum, Litecoin, and Monero, among others.

In conclusion, Bitcoin is a decentralized digital currency that operates on a blockchain. Its decentralized nature, use of cryptography, and lack of central control make it a secure and private form of currency that has gained popularity globally.




################################################
## Here is the result of the search for [Bitcoin]
################################################

Summary: Bitcoin is a decentralized digital currency that allows for peer-to-peer transactions without the need for intermediaries like banks. It was created in 2009 by an anonymous individual or group using the pseudonym Satoshi Nakamoto.

Detailed Explanation:

Bitcoin is a decentralized digital currency that operates on a blockchain, a public ledger that records all transactions. The network is decentralized, meaning there is no central authority controlling it. Transactions are verified by network nodes through cryptographic algorithms, and once confirmed, the transactions are added to the blockchain.

The Bitcoin protocol allows for peer-to-peer transactions without the need for intermediaries like banks. Users can generate their own bitcoins through a process called mining, where they solve complex mathematical problems to validate transactions and add them to the blockchain. Once generated, bitcoins can be transferred between users using specialized software or hardware.

Bitcoin's decentralized nature and use of cryptography make it a secure form of currency. The blockchain technology that underlies Bitcoin provides a tamper-proof record of all transactions, ensuring that the integrity of the network is maintained.

The lack of central control also makes Bitcoin immune to government manipulation or censorship. Transactions are pseudonymous, allowing users to maintain their privacy and avoid government tracking.

Bitcoin's decentralized nature has led to its adoption in various industries, such as finance, gaming, and e-commerce. It has also sparked the development of other cryptocurrencies, such as Ethereum, Litecoin, and Monero, among others.

In conclusion, Bitcoin is a decentralized digital currency that operates on a blockchain. Its decentralized nature, use of cryptography, and lack of central control make it a secure and private form of currency that has gained popularity globally.
kfukaya@kfukaya:~/projects/ai/CrewAIWithOllama$

```
(Note) The response from the model could be different even you specify the same keyword for input. This is the nature of the LLM, but the context should be similar.
