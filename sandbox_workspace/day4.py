import chromadb

client = chromadb.PersistentClient(path = "./chroma_sandbox")

collection = client.create_collection(name = "test_products")


collection.add(
    documents=[
        "Night Repair Cream with retinol for anti-aging",
        "Vitamin C serum for brightening skin",
        "Free shipping on orders over $50"
    ],
    ids=["prod_1", "prod_2", "policy_1"]
)

results = collection.query(
    query_texts=["What helps with aging skin?"],
    n_results=2
)

print("Query: 'What helps with aging skin?'")
print(f"Top result: {results['documents'][0][0]}")
print(f"Second result: {results['documents'][0][1]}")
print(f"Distance scores: {results['distances'][0]}")

# 5. Clean up — delete the collection (optional)
client.delete_collection("test_products")