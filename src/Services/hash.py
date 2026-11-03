import hashlib

class HashServices():

    @staticmethod
    def criptografar(texto: str) -> str:
        texto_bytes = texto.encode('utf-8')

        return hashlib.sha256(texto_bytes).hexdigest()

    @staticmethod
    def verficar_hash(texto: str, texto_hash: str) -> bool:
        novo_hash = HashServices.criptografar(texto)

        return novo_hash == texto_hash