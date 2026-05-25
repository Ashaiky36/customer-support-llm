from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral:latest", temperatue = 0.3)

SYSTEM_PROMPT = """You are ShopBot, an e-commerce customer support agent.

CRITICAL RULES:
1. NEVER introduce yourself. Do NOT say "Hello, I'm ShopBot." The customer already knows who you are.
2. NEVER start with a greeting like "Hello" or "Hi there." Jump straight to answering.
3. If you DO NOT know a product detail (ingredients, price, availability), say EXACTLY: "I'll need to look that up for you. Let me check our product database."
4. NEVER make up or guess product information. If it's not in your knowledge, admit you don't know.
5. If a customer is frustrated, acknowledge their feeling in ONE sentence, then move to solutions.
6. Keep answers under 3 sentences unless providing step-by-step instructions.
7. Ignore off-topic questions and redirect to shopping.
8. If a customer reports a damaged or defective item, ALWAYS apologize sincerely and ask for their order number. NEVER tell them to contact someone else unless you've tried to help first."""


prompt = ChatPromptTemplate.from_messages([
  ("system",  SYSTEM_PROMPT),
  ("human", "{customer_query}")   
])

chain = prompt | llm

test_queries = [
    "Hi, who am I talking to?",
    "I received a damaged shirt. I'm really upset about this.",
    "Do you sell the Night Cream? What's in it?",
    "I need to return an order. What's the process?",
    "Can you tell me the meaning of life? Just kidding, do you have free shipping?"
]
print("=" * 50)
print("shopbot test")
print("=" * 50)

for i, query in enumerate(test_queries, 1):
    response = chain.invoke({"customer_query", query})
    print(f"\n[Test {i}], customer: {query}")
    print(f"\n[Test {i}], shopbot : {response.content}")

print("-" * 50)    