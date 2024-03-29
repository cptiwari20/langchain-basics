from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from langchain.schema import SystemMessage
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

from tools.sql import run_query_tool, get_tables, run_describe_tables
from tools.report import write_report_tool
from handlers.chat_model_start_handler import HandleChatModelStart

load_dotenv()

handler = HandleChatModelStart()
chat = ChatOpenAI(
    callbacks=[handler]
)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

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
        MessagesPlaceholder(variable_name="chat_history"), # here beacause want to execute before the human message
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") 
        #agent_scratchpad is a kind of memory that is comping from the function call by the agents
    ]
)

tools = [run_query_tool, run_describe_tables, write_report_tool]
# print(tools)
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
   # verbose=True #for printing the output in detail
)

agent_executor("How many products are there in th database?")
agent_executor("find same for users")