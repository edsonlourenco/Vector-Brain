"""Module database utility functions for handling document vectorization and retrieval."""

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.settings import Session


class DocumentVectorizer:
    """Class to handle document loading and vectorization.

    Returns:
        list: A list of text chunks from the PDF document.
    """
    def load_split_pdf(self, pdf_path, chunk_size=1000, chunk_overlap=150) -> list[str]:
        """Load a PDF document and split it into text chunks."""
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return text_splitter.split_documents(documents)
    
    def create_vector_store(self, texts: list[str], session: Session) -> any:
        """Create a vector store from the text chunks."""
        embeddings = OpenAIEmbeddings(openai_api_key=session.OPENAI_API_KEY)
        db = FAISS.from_documents(texts, embeddings)
        return db.as_retriever()