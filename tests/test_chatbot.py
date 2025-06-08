"""Test cases for OpenAIChatBot class
"""

from unittest.mock import patch, MagicMock
from utils.chatbot import OpenAIChatBot


def test_init_sets_llm():
    with patch("utils.chatbot.ChatOpenAI") as mock_chat:
        bot = OpenAIChatBot("fake-key", temperature=0.7)
        mock_chat.assert_called_once_with(openai_api_key="fake-key", temperature=0.7)
        assert hasattr(bot, "llm")

def test_get_chain_returns_chain():
    mock_llm = MagicMock()
    mock_retriever = MagicMock()
    mock_chain = MagicMock()
    with patch("utils.chatbot.ChatOpenAI", return_value=mock_llm):
        with patch("langchain.chains.RetrievalQA.from_chain_type", return_value=mock_chain) as mock_from_chain:
            bot = OpenAIChatBot("fake-key")
            chain = bot.get_chain(mock_retriever)
            mock_from_chain.assert_called_once_with(
                llm=mock_llm,
                retriever=mock_retriever,
                chain_type="stuff"
            )
            assert chain == mock_chain

def test_start_chat_exit(monkeypatch):
    mock_chain = MagicMock()
    mock_chain.run.return_value = "Resposta"
    mock_retriever = MagicMock()
    with patch.object(OpenAIChatBot, "get_chain", return_value=mock_chain):
        bot = OpenAIChatBot("fake-key")
        inputs = iter(["sair"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        with patch("builtins.print") as mock_print:
            bot.start_chat(mock_retriever)
            assert any("Encerrando" in str(call) for call in mock_print.call_args_list)
