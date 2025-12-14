from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['LANGCHAIN_PROJECT']='Sequential llm app'

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

# Groq LLM
model_1 = ChatGroq(
    model="openai/gpt-oss-120b",   # simple + fast
    temperature=0.7
)

model_2 = ChatGroq(
    model="openai/gpt-oss-20b",   # simple + fast
    temperature=0.5
)


parser = StrOutputParser()

chain = prompt1 | model_2 | parser | prompt2 | model_1 | parser


config={
    'run_name':'sequential chain',
    'tags': ['llm app' , 'report generation' , 'summarization'],
    'metadata': {'model_1': 'openai/gpt-oss-120b' , 'parser':'strOutputparser' }
}


result = chain.invoke({'topic': 'Unemployment in India'} , config=config)

print(result)
