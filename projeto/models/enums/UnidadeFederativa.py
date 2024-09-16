from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia","BA")
    SAO_PAULO = ("SÃO PAULO","SP")
    RIO_DE_JANEIRO = ("RIO DE JANEIRO","RJ")

    def __init__(self,nome:str,caracter:str) -> None:
        self.nome = nome
        self.caracter = caracter