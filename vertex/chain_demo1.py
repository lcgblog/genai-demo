from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import VertexAI
from vertex_client import VertexClient

client = VertexClient()

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = VertexAI(temperature=0.1, model_name="gemini-1.5-flash-001", max_tokens=1000, max_retries=0)
output_parser = StrOutputParser()

chain = prompt | model | output_parser

res = chain.invoke({"topic": "ice cream"})
print(res)