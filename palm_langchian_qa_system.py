from dotenv import load_dotenv
from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

import os


load_dotenv()  # take environment variables from .env (especially google api key)

# Create Google Palm LLM model
"""
temperature=0.2: This sets the temperature parameter for the LLM. Temperature controls the randomness of the LLM's outputs. A lower temperature (like 0.2) leads to more conservative and deterministic responses, while a higher temperature increases creativity and risk of unexpected outputs. The optimal temperature setting depends on your specific use case and desired outcome.
"""
llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)


# Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(
    model_name="hkunlp/instructor-large")


def initialize_chroma_vector_store():
    # Loading the csv file data
    loader = CSVLoader(file_path="faqs_codebasics.csv", source_column="prompt")
    data = loader.load()
    # Initialize Chromadb vector store
    vectordb = Chroma.from_documents(data,
                                     embedding=instructor_embeddings,
                                     persist_directory='./chromadb')

    # Persist the vector store to disk
    vectordb.persist()


def get_qa_chain():
    # Load from the disk
    vectordb = Chroma(persist_directory='./chromadb',
                      embedding_function=instructor_embeddings)
    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "Sorry it is beyond my knowledge. For more info contact abc@gmail.com  " Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # another one is map reduce that was used in URL
        retriever=retriever,
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT})

    return chain


if __name__ == "__main__":
    initialize_chroma_vector_store()
    chain = get_qa_chain()
    print(chain("Do you guys provide internship and also do you offer EMI payments?"))
