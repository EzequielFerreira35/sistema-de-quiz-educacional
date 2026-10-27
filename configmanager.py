import json
from pathlib import Path

class ConfigManager:
    """Classe responsável com gerenciar o arquivo config.json"""
    
    _CAMINHO_JSON = Path(__file__).parent / "config.json"
    def __init__(self):
        self.caminho = self._CAMINHO_JSON

    def _read(self) -> dict:
        if not self.caminho.exists():
            return {}
        with open(self.caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        return dados

    @property
    def quiz_duracao(self) -> int:
        dados =  self._read()
        return dados.get("quiz", {}).get("quiz_duracao", 0)

    @property
    def max_tentativas_por_quiz(self) -> int:
        dados = self._read()
        return dados.get("tentativa", {}).get("numero_max_tentativas_por_quiz", 0)

    @property
    def pergunta_peso(self) -> dict:
        dados = self._read()
        return dados.get("pergunta", {}).get("peso")

    @property
    def qtd_alternativas(self) -> list:
        dados = self._read()
        return dados.get("pergunta", {}).get("qtd_alternativas", 0)

    def atualizar_config(self, chave_principal, subchave, valor) -> bool:
        dados = self._read

        if chave_principal or subchave not in dados:
            return False

        dados[chave_principal][subchave] = valor

        with open(self.caminho, 'r', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
