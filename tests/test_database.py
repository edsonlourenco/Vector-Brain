"""Test cases for the DocumentVectorizer class in utils.database module.
"""

from unittest.mock import patch, MagicMock
from utils.database import DocumentVectorizer
from utils.settings import Session


def test_load_split_pdf_splits_text(monkeypatch):
    mock_documents = ["doc1", "doc2"]
    mock_chunks = ["chunk1", "chunk2", "chunk3"]

    mock_loader = MagicMock()
    mock_loader.load.return_value = mock_documents

    mock_splitter = MagicMock()
    mock_splitter.split_documents.return_value = mock_chunks

    with patch("utils.database.PyPDFLoader", return_value=mock_loader):
        with patch("utils.database.RecursiveCharacterTextSplitter", return_value=mock_splitter):
            vectorizer = DocumentVectorizer()
            result = vectorizer.load_split_pdf("fake.pdf")
            assert result == mock_chunks
            mock_loader.load.assert_called_once()
            mock_splitter.split_documents.assert_called_once_with(mock_documents)

def test_create_vector_store_returns_retriever(monkeypatch):
    mock_embeddings = MagicMock()
    mock_db = MagicMock()
    mock_retriever = MagicMock()
    mock_db.as_retriever.return_value = mock_retriever

    with patch("utils.database.OpenAIEmbeddings", return_value=mock_embeddings):
        with patch("utils.database.FAISS.from_documents", return_value=mock_db):
            vectorizer = DocumentVectorizer()
            session = Session()
            texts = ["text1", "text2"]
            retriever = vectorizer.create_vector_store(texts, session)
            assert retriever == mock_retriever
            mock_db.as_retriever.assert_called_once()
