"""
Main script to run the LLM assistant for PDF document processing and chat interaction."
"""

from langchain.chains import RetrievalQA

from colorama import Fore, Style

from utils.settings import Session
from utils.database import DocumentVectorizer
from utils.chatbot import OpenAIChatBot


def initialize_instances() -> tuple[Session, DocumentVectorizer, OpenAIChatBot]:
    """Initialize instances of Session, DocumentVectorizer, and OpenAIChatBot."""
    session = Session()
    docvectorizer = DocumentVectorizer()
    openaichatbot = OpenAIChatBot(openai_api_key=session.OPENAI_API_KEY)
    return session, docvectorizer, openaichatbot

def main():
    """Main function to run the LLM assistant."""

    session, docvectorizer, openaichatbot = initialize_instances()

    print(f"{Fore.YELLOW}📄 Carregando e dividindo o PDF...{Style.RESET_ALL}")
    texts = docvectorizer.load_split_pdf(session.PDF_PATH)
    
    print(f"{Fore.BLUE}🧠 Gerando embeddings e criando o índice vetorial...{Style.RESET_ALL}")
    retriever = docvectorizer.create_vector_store(texts, session)

    print(f"{Fore.GREEN}💬 Inicializando o modelo de chat...{Style.RESET_ALL}")
    openaichatbot.start_chat(retriever)


if __name__ == "__main__":
    main()