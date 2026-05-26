# from langchain_community.document_loaders import TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json
import os

file_path = "data/sample_products.txt"
output_path = "data/chunks.json"

CHUNK_SIZE = 900
CHUNK_OVERLAP = 90
SEPARATORS = ["\n---\n","\n\n", "\n", "Q:", "Shipping Policy:", ". ", " ", ""]

print("day3: data loading and text splitting pipelinee")
print(f"document loading from: {file_path}")

loader = TextLoader(file_path, encoding = "utf-8")
document = loader.load()

print("document loaded")
print(f"no. of pages in document: {len(document)}")
print(f"total no. of characters: {len(document[0].page_content):,}")

print("text splitter configuration")
print(f"chunk size : {CHUNK_SIZE}")
print(f"chunk overlap : {CHUNK_OVERLAP}")
print(f"separators used : {SEPARATORS}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = CHUNK_SIZE,
    chunk_overlap =CHUNK_OVERLAP,
    separators = SEPARATORS,
    length_function = len,
    add_start_index = True
)

chunks = text_splitter.split_documents(document)
print("splitting done")
print(f"no. of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    chunk_length = len(chunk.page_content)
    start_index = chunk.metadata.get("start_index", "N/A")

    preview = chunk.page_content[:150].replace("\n", " ↵ ")

    print(f"chunk {i+1:2d} | length: {chunk_length:4d} | start index: {start_index}")
    print(f"{preview}.....")



chunk_data = []
for i, chunk in enumerate(chunks):
    chunk_data.append({
        "chunk_id": i,
        "text" : chunk.page_content,
        "char_count" : len(chunk.page_content),
        "meta_data" : {
            "sources" : chunk.metadata.get("source", file_path),
            "start_index" : chunk.metadata.get("start_index", 0)
        }

    })

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(chunk_data, f, indent=2, ensure_ascii=False)    

print(f"\n{'=' * 65}")
print(f"PIPELINE COMPLETE")
print(f"{'=' * 65}")
print(f"  Input:  {file_path}")
print(f"  Output: {output_path}")
print(f"  Chunks saved: {len(chunk_data)}")    