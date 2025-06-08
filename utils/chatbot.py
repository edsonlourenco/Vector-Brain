"""Module chatbot utilities for interacting with the OpenAI API."""

from langchain_community.chat_models import ChatOpenAI
from colorama import Fore, Style


class OpenAIChatBot:

    def __init__(self, openai_api_key, temperature=0.3):
        """Initialize the OpenAI chatbot with API key and temperature."""
        self.llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=temperature)
    
    def get_chain(self, retriever):
        """Get the RetrievalQA chain with the LLM and retriever."""
        from langchain.chains import RetrievalQA
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=retriever,
            chain_type="stuff"
        )
    
    def start_chat(self, retriever):
        """Start the chat loop with the user."""
        print(f"{Fore.CYAN}🚀 Pronto! Pergunte algo sobre o PDF:{Style.RESET_ALL}")
        qa_chain = self.get_chain(retriever)
        while True:
            query = input(f"{Fore.MAGENTA}🤔 Você: {Style.RESET_ALL}")
            if query.lower() in ["sair", "exit", "quit"]:
                print(f"{Fore.RED}👋 Encerrando...{Style.RESET_ALL}")
                break
            result = qa_chain.run(query)
            print(f"{Fore.GREEN}💡 Assistente: {result}{Style.RESET_ALL}")