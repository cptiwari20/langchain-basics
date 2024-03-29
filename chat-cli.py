from langchain.chains import LLMChain
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory, ConversationSummaryMemory
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(verbose=True)

# memory = ConversationBufferMemory(
#     chat_memory=FileChatMessageHistory('message.json'), #this will store the history in file
#     memory_key="message", 
#     return_messages=True
#     )
#memory key is the object key that we want to assign to the conversational data.
#return messages is for returning the previous messages in the memory so that we can reuse for the next conversation.

memory = ConversationSummaryMemory(
    llm=chat,
    memory_key="message",
    return_messages=True
)

prompt = ChatPromptTemplate(
    input_variables=["content", "message"], #content is from the user input and message from the memory
    messages=[
        MessagesPlaceholder(variable_name="message"), #variable name here is coming from the memory, the memory key that we had put
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True
)

print("Please ask whatever you want to ask with the OpenAI Chatbot!")
while True:
    content = input(">>> ")
    response = chain({"content": content})
    print(response['text'])
