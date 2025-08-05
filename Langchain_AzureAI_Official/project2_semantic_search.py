from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.runnables import chain
from embedding_model import get_embedding_by_model

file_path = "/Users/sarangia/Desktop/Master/Learning/Gen AI/Public/pdf/nke-10k-2023.pdf"

loader = PyPDFLoader(file_path)
docs = loader.load()

print(len(docs))

print(f"{docs[0].page_content[:50]}\n")

print(docs[0].metadata)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
    add_start_index = True
)

all_splits = text_splitter.split_documents(docs)

print(len(all_splits))
print(f"Length of first split: {len(all_splits[0].page_content)}")
print(f"{all_splits[0].page_content[:50]}\n")

#getting embadding based on provider type
embedding = get_embedding_by_model('openai')

# inMemoryvectorstore

vector_store = InMemoryVectorStore(embedding)

ids = vector_store.add_documents(all_splits)

@chain
def retriver(query: str):
    return vector_store.similarity_search(query, k=1)

res = retriver.invoke('How many distribution centers does Nike have in the US?')

#for executing batch

res = retriver.batch([
     "How many distribution centers does Nike have in the US?",
    "When was Nike incorporated?",
])
print('Final Result --> ', res) #[[[]], [[]]]
print('Final Result1 --> ', res[0])# [[]]
print('Final result2 _____>', res[0][0].page_content) # Final response