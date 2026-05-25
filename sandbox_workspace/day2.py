from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

template = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful {persona}"),
    ("human", "{user_input}")
])

model = ChatOllama(model = "mistral:latest")

chain = template | model

result = chain.invoke({
    "persona" : "kindergarten teahcer",
    "user_input" : "what is el nino?"
})

print(result.content)