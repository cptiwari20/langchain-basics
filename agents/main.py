from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.prompts import (
    PromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

prompt = PromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") 
        #agent_scratchpad is a kind of memory that is comping from the function call by the agents
    ]
)

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=[]
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[],
    verbose=True #for printing the output in detail
)

agent_executor("What is the database?")