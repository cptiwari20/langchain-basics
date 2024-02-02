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

print("Finding Answer for {{args.task}}, please wait...")
# result = llm.invoke("how can langsmith help with testing?")

prompt_template = PromptTemplate(
    template="Write a very simple {language} funtion that will {task}",
    input_variables= ["language", "task"]
)

new_chain = LLMChain(
    prompt=prompt_template,
    llm=llm,
    output_key="code"
)

result = new_chain({
    "language": args.language,
    "task": args.task
})

print(result)
