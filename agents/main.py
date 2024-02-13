from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from langchain.schema import SystemMessage
from dotenv import load_dotenv

from tools.sql import run_query_tool, get_tables, run_describe_tables

load_dotenv()

chat = ChatOpenAI()

tables = get_tables()
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(
            "Assume you are using sqlite database with tables "
            f"The database has table names of: {tables}\n"
            "Do not make any assumption what table name exists "
            "or what column exists; Instead use 'describe_table' function tool"

            )
        ),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") 
        #agent_scratchpad is a kind of memory that is comping from the function call by the agents
    ]
)

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=[run_query_tool, run_describe_tables]
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[run_query_tool, run_describe_tables],
    verbose=True #for printing the output in detail
)

agent_executor("Does user have one or more shipping addresses each?")