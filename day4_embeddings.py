from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
import shutil

DATA_PATH = "data/sample_products.txt"
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "ecommerce_products"

loader = TextLoader(DATA_PATH, encoding = "utf-8")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 900,
    chunk_overlap = 80,
    separators = ["\n\n", "\n", "Q:", "Shipping Policy:", ". ", " ", ""],
    add_start_index = True
)

chunks = text_splitter.split_documents(documents)

print(f"{len(chunks)} text chunks generated")

print("initializing the embedding engine")

embeddings = OllamaEmbeddings(model = "nomic-embed-text")

test_vector = embeddings.embed_query("testing my local ollama model")

print(f"vector dimensions: {len(test_vector)}")
print(f"sample vector array preview: {test_vector[:3]}")

print("creating and saving vector store")

if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)
    #it deletes existing chromadb if it existss

vector_store = Chroma.from_documents(
    documents = chunks,
    embedding = embeddings,
    collection_name = COLLECTION_NAME,
    persist_directory = CHROMA_PATH
)    

print(f"database created at: {CHROMA_PATH}")
print(f"indexed_count: {vector_store._collection.count()}")


print("testing semantic similarity retrieval ")

# retriever = vector_store.as_retriever(
#     search_type = "similarity_score_threshold", #performs a similarity search but has different search
#     search_kwargs = {
#         "k": 3,
#         "score_threshold" : 0.3
                     
#                      } #takes top 2 results
# )

# def search_with_scores(query, retriever):
#     results = vector_store.similarity_search_with_relevance_scores(query, k =3)

#     print(f"query = {query}")
#     if not results:
#         print(f"no results above the threshold")
#         return
    
#     for i, (doc, score) in enumerate(results):
#         preview = doc.page_content[:120].replace("\n", " | ")
#         indicator = "✅" if score >= 0.5 else "⚠️" if score >= 0.3 else "❌"
#         print(f"  {indicator} Rank {i+1} (score: {score:.3f}): {preview}...")

# test_queries = [
#     "What are the side effects of the night cream?",
#     "Can I return a product if I don't like it?",
#     "How much does shipping cost?"
# ]

# for query in test_queries:
#     results = retriever.invoke(query)
#     print(f"ques. asked: {query}")
#     preview = results[0].page_content[:120].replace("\n", "|")
#     print(f"top match: {preview}")


# test_queries = [
#     "What are the side effects of the night cream?",
#     "Is the Vitamin C serum good for brightening?",
#     "Can I return a product if I don't like it?",
#     "How much does shipping cost?",
#     "Is this safe for pregnancy?",
#     "Do you test on animals?",
#     "How long does a bottle last?"
# ]

# for query in test_queries:
#     search_with_scores(query, retriever)
    
#     print(f"\n  Query: '{query}'")
#     print(f"  Top match: {results[0].page_content[:100].replace(chr(10), ' | ')}...")
#     if len(results) > 1:
#         print(f"  2nd match: {results[1].page_content[:100].replace(chr(10), ' | ')}...")
#     print(f"  Source location: index {results[0].metadata.get('start_index', 'unknown')}")

test_queries = [
    "What are the side effects of the night cream?",
    "Is the Vitamin C serum good for brightening?",
    "Can I return a product if I don't like it?",
    "How much does shipping cost?",
    "Is this safe for pregnancy?",
    "Do you test on animals?",
    "How long does a bottle last?"
]

for query in test_queries:
    # Use the vectorstore directly — returns (document, score) tuples
    results = vector_store.similarity_search_with_relevance_scores(query, k=3)
    
    print(f"\n  Query: '{query}'")
    
    # Filter by score threshold
    filtered = [(doc, score) for doc, score in results if score >= 0.25]
    
    if not filtered:
        print(f"  ⚠️  No results above confidence threshold (0.3)")
        continue
    
    for rank, (doc, score) in enumerate(filtered, 1):
        preview = doc.page_content[:100].replace("\n", " | ")
        indicator = "✅" if score >= 0.5 else "⚠️"
        print(f"  {indicator} Rank {rank} (score: {score:.3f}): {preview}...")
