# 🤖 Vector Brain - Chatbot com LLM e Vetorização de PDF

Bem-vindo ao **Vector Brain**! Este projeto demonstra como criar um chatbot inteligente usando modelos de linguagem (LLM) e vetorização de documentos PDF. O objetivo é permitir perguntas e respostas contextuais sobre um e-book técnico, utilizando IA de ponta.

## 📚 Documento Utilizado

O PDF vetorizado é o e-book oficial gratuito da Databricks (versão PT-BR):  
[TAP FULL POTENTIAL LLM - Databricks](https://www.databricks.com/br/resources/ebook/tap-full-potential-llm?scid=7018Y000001Fi0cQAC&utm_medium=paid+search&utm_source=google&utm_campaign=20613856692&utm_adgroup=160163579880&utm_content=ebook&utm_offer=tap-full-potential-llm&utm_ad=687639151367&utm_term=modelos%20de%20linguagem%20grandes&gad_source=1&gad_campaignid=20613856692&gbraid=0AAAAABYBeAhja7JrujV1Gwa5wnSWhEQ2J&gclid=CjwKCAjw6ZTCBhBOEiwAqfwJd83xaDMopGbPakJcHmZJqEObU3PSfAa0nQU2TmdQ7HKLvOhngvWF-RoC_5IQAvD_BwE)

## ✨ Demonstração

Veja abaixo algumas cenas do projeto em funcionamento:

![Demo 1](static/demo/demo-1.png)
> **Cena 1:** Inicialização do chatbot e carregamento do documento PDF vetorizado.

![Demo 2](static/demo/demo-2.png)
> **Cena 2:** Usuário faz uma pergunta sobre o conteúdo do e-book e recebe uma resposta contextualizada.

![Demo 3](static/demo/demo-3.png)
> **Cena 3:** Demonstração do encerramento da sessão de chat com mensagem amigável.

## 🚀 Como Usar

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/Vector-Brain.git
   cd Vector-Brain
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure sua chave da OpenAI**
   - Crie um arquivo `.env` na raiz do projeto com o conteúdo:
     ```
     OPENAI_API_KEY=sua-chave-openai-aqui
     ```

5. **Execute a aplicação**
   ```bash
   python main.py
   ```

6. **Interaja com o chatbot**
   - Faça perguntas sobre o conteúdo do e-book diretamente no terminal.
   - Para sair, digite `sair`, `exit` ou `quit`.

## 🧪 Como Testar

Execute todos os testes automatizados com:
```bash
pytest
```

## 🛠️ Estrutura do Projeto

- `utils/` — Módulos utilitários (chatbot, database, settings)
- `tests/` — Testes automatizados
- `docs/` — PDF
- `static/demo/` — Imagens de demonstração

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou pull requests!

---

Feito com 💙 por Edson Lourenço
