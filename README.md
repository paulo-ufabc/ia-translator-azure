# 🌐 Article Translator App

Este projeto é uma aplicação simples e modular que permite extrair texto de artigos na web e traduzi-los para qualquer idioma usando a API Azure OpenAI. Foi desenvolvido seguindo os princípios **SOLID** e **Clean Code**, ideal para aprender boas práticas e criar soluções escaláveis.

## 📖 Funcionalidades

* 🔍 **Extração de Texto**: Obtém o conteúdo textual limpo de qualquer URL fornecida
* 🌎 **Tradução de Idiomas**: Traduz o texto extraído para o idioma desejado usando a Azure OpenAI
* 🛠️ **Modularidade**: Código estruturado em classes para facilitar manutenção e extensão
* 🧹 **Boas Práticas**: Aplicação de princípios **SOLID**, **Clean Code** e tratamento de exceções detalhado

## 🚀 Como Rodar o Projeto

### ⚙️ Pré-requisitos

* Python 3.8+
* Uma conta na **Azure OpenAI** com um endpoint configurado
* Virtualenv para gerenciar dependências (opcional)

### 📦 Instalação

1. Clone o repositório:
```bash
gh repo clone paulo-ufabc/ia-translator-azure
cd ia-translator-azure
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
   
   Crie um arquivo `.env` no diretório raiz com o seguinte conteúdo:
```env
AZURE_ENDPOINT=https://seu-endpoint.azure.com/
AZURE_OPENAI_KEY=sua-api-key
```

### 🖥️ Como Usar

1. Modifique a URL e o idioma de destino no arquivo principal (`main.py`):
```python
URL = "url aqui"
TARGET_LANGUAGE = "português"
```

2. Execute o aplicativo:
```bash
python main.py
```

3. Veja a tradução diretamente no terminal! 🎉

## 📂 Estrutura do Projeto

```
article-translator-app/
├── main.py            # Ponto de entrada principal
├── extractor.py       # Lógica para extrair texto de uma URL
├── translator.py      # Serviço de tradução usando Azure OpenAI
├── config.py          # Configurações da API
├── requirements.txt   # Dependências do projeto
└── .env_._example      # Exemplo de arquivo de variáveis de ambiente
```

## ✨ Tecnologias Usadas

* **BeautifulSoup**: Para extração e manipulação de HTML
* **Requests**: Para requisições HTTP
* **Azure OpenAI**: Para tradução de texto

## 🛡️ Boas Práticas

* **Princípios SOLID**: Cada classe tem uma responsabilidade única
* **Clean Code**: Código legível, modular e fácil de manter
* **Variáveis de ambiente**: Segurança para dados sensíveis, como chaves de API

## 📋 Tarefas Futuras

* Adicionar suporte para mais APIs de tradução
* Criar uma interface gráfica (GUI) simples para facilitar o uso
* Implementar testes unitários com cobertura total

## 🤝 Contribuições

Contribuições são muito bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um fork do repositório
2. Crie um branch para sua feature ou correção:
```bash
git checkout -b minha-feature
```

3. Envie suas alterações:
```bash
git commit -m "Adiciona minha nova feature"
git push origin minha-feature
```

4. Abra um Pull Request 🚀

## 📧 Contato

Criado com ❤️ por **Paulo Nascimento**. Dúvidas ou sugestões? Entre em contato: **paulo.abreu@aluno.ufabc.edu.br**