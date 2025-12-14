# import os
# from dotenv import load_dotenv
# from langchain_community.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import (
#     RunnableParallel,
#     RunnablePassthrough,
#     RunnableLambda
# )
# from langchain_core.output_parsers import StrOutputParser
# from langchain_groq import ChatGroq

# os.environ['LANGCHAIN_PROJECT']='RAG Chatbot'

# # Load environment variables
# load_dotenv()  # expects GROQ_API_KEY

# PDF_PATH = "islr.pdf"  # <-- your PDF file

# # 1) Load PDF
# loader = PyPDFLoader(PDF_PATH)
# docs = loader.load()  # one Document per page

# # 2) Chunk documents
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=150
# )
# splits = splitter.split_documents(docs)

# # 3) Embeddings (all-MiniLM-L6-v2)
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # 4) Vector store
# vectorstore = FAISS.from_documents(splits, embeddings)
# retriever = vectorstore.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 4}
# )

# # 5) Prompt
# prompt = ChatPromptTemplate.from_messages([
#     (
#         "system",
#         "Answer ONLY from the provided context. "
#         "If the answer is not present, say you don't know."
#     ),
#     (
#         "human",
#         "Question: {question}\n\nContext:\n{context}"
#     )
# ])

# # 6) Groq LLM
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",  # or mixtral-8x7b, deepseek-r1-distill-llama-70b
#     temperature=0
# )

# # Helper to format retrieved docs
# def format_docs(docs):
#     return "\n\n".join(d.page_content for d in docs)

# # 7) Chain
# parallel = RunnableParallel({
#     "context": retriever | RunnableLambda(format_docs),
#     "question": RunnablePassthrough()
# })

# chain = parallel | prompt | llm | StrOutputParser()

# # 8) Ask questions
# print("📄 PDF RAG ready with Groq + MiniLM embeddings")
# print("Ask a question (Ctrl+C to exit)")

# while True:
#     q = input("\nQ: ").strip()
#     if not q:
#         continue
#     ans = chain.invoke(q)
#     print("\nA:", ans)


import torch
print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
