from bs4 import BeautifulSoup
import requests

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