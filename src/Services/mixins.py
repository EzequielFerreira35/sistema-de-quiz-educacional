class ValidadorIdMixin:
    def _validar_id(self, valor: str, nome: str) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{nome} deve ser uma string não vazia")

        return valor.strip()