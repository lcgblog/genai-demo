from functools import partial
from vertexai.generative_models import GenerativeModel
from langchain_core.messages import HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.chains.llm import LLMChain
from langchain_google_vertexai import VertexAI
from vertex_client import VertexClient

client = VertexClient()
model = VertexAI(temperature=0.1, model_name="gemini-1.5-flash-001", max_tokens=1000, max_retries=0)
result = model.invoke("tell me a joke")
print("Joke: ", result)

chat_template = ChatPromptTemplate.from_messages([
    HumanMessage(
        content=(
            "return the sentiment for the given text in json format the sentiment value can be 'negative', 'positive'"
        )
    ),
    HumanMessagePromptTemplate.from_template('{text}')
])

chat_message = chat_template.format_messages(text="i don't like weather today.")
chain = LLMChain(llm=model, prompt=chat_template, verbose=True)
res = chain.invoke(chat_message)
print("i don't like weather today.. res:", res)
