from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
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

test_template = PromptTemplate(
    template="Write a very simple {language} test code for the {code}",
    input_variables= ["language", "code"]
)

first_chain = LLMChain(
    prompt=prompt_template,
    llm=llm,
    output_key="code"
)
second_chain = LLMChain(
    prompt=test_template,
    llm=llm,
    output_key="test"
)

chain = SequentialChain(
    chains=[first_chain, second_chain],
    input_variables=['language', 'task'],
    output_variables=['code', 'test']
)

result = chain({
    "language": args.language,
    "task": args.task
})

print('>>> CODE Generated <<<<')
print(result['code'])
print('>>> Test Generated <<<<')
print(result['test'])
