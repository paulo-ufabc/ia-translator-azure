from extractor import ArticleExtractor
from config import AzureAIConfig
from translator import TranslatorService


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
