from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Write a number from 1 to 10")
parser.add_argument('--language', default="JavaScript")
args = parser.parse_args()

llm = ChatOpenAI()

print("Finding Answer, please wait...")
result = llm.invoke("how can langsmith help with testing?")

prompt_template = PromptTemplate(
    template="Write a code in {language} where you have to {task}",
    input_variables= ["language", "task"]
)

new_chain = LLMChain(
    prompt=prompt_template,
    llm=llm
)

result = new_chain({
    "language": "JavaScript",
    "task": "Write a number from 1 to 10"
})

print(result)
