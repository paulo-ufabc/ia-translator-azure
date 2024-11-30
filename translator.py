
import requests
from config import AzureAIConfig

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