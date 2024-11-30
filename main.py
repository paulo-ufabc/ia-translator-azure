from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração da API
class AzureAIConfig:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_ENDPOINT")
        self.api_key = os.getenv("AZURE_OPENAI_KEY")

# Serviço de extração de texto
class ArticleExtractor:
    def __init__(self, url: str):
        self.url = url

    def extract_text(self) -> str:
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            self._remove_unnecessary_tags(soup)
            return soup.get_text(" ", strip=True)
        else:
            raise Exception(f"Falha ao buscar a URL. Código de status: {response.status_code}")

    @staticmethod
    def _remove_unnecessary_tags(soup):
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

# Serviço de tradução
class TranslatorService:
    def __init__(self, config: AzureAIConfig):
        self.endpoint = config.endpoint
        self.api_key = config.api_key

    def translate_text(self, text: str, target_language: str) -> str:
        payload = self._build_payload(text, target_language)
        headers = self._build_headers()

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            return self._parse_response(response)
        except requests.RequestException as e:
            raise Exception(f"Erro ao realizar a requisição de tradução. Detalhes: {e}")

    def _build_payload(self, text: str, lang: str) -> dict:
        return {
            "messages": [
                {"role": "system", "content": [{"type": "text", "text": "Você atua como tradutor de textos"}]},
                {"role": "user", "content": [{"type": "text", "text": f"traduza: {text} para o idioma {lang} e responda apenas com a tradução no formato markdown"}]},
            ],
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 900,
        }

    def _build_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }

    @staticmethod
    def _parse_response(response) -> str:
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', '')

# Ponto de entrada principal
class ArticleTranslatorApp:
    def __init__(self, url: str, target_language: str):
        self.url = url
        self.target_language = target_language

    def run(self):
        try:
            print("Iniciando a extração do texto...")
            article_text = ArticleExtractor(self.url).extract_text()

            print("Texto extraído com sucesso. Iniciando a tradução...")
            config = AzureAIConfig()
            translated_text = TranslatorService(config).translate_text(article_text, self.target_language)

            print("Tradução realizada com sucesso. Resultado:")
            print(translated_text)
        except Exception as e:
            print(f"Erro durante a execução: {e}")

# Execução
if __name__ == "__main__":
    URL = "article_aqui"
    TARGET_LANGUAGE = "português"
    app = ArticleTranslatorApp(URL, TARGET_LANGUAGE)
    app.run()
