import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração da API
class AzureAIConfig:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_ENDPOINT")
        self.api_key = os.getenv("AZURE_OPENAI_KEY")