from models.enums import sexo
from models.endereco import Endereco


class Pessoa:
    def __init__(self,id:int,nome:str,dataNascimento:str,telefone:str,email:str,sexo:sexo,endereco:Endereco) -> None:
        self.id=id
        self.nome= nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self. sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return(f"\nID:{self.id} \nNome:{self.nome} \nData Nascimento:{self.dataNascimento} ,\nTelefone:{self.telefone} \nEmail:{self.email} \nSexo:{self.sexo} \nEndereço:{self.endereco}")
    