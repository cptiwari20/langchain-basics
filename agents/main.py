from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)
from dotenv import load_dotenv

from tools.run_query_tool import run_query_tool

load_dotenv()

chat = ChatOpenAI()

prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") 
        #agent_scratchpad is a kind of memory that is comping from the function call by the agents
    ]
)

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=[run_query_tool]
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[run_query_tool],
    verbose=True #for printing the output in detail
)

agent_executor("How many shipping address in database?")