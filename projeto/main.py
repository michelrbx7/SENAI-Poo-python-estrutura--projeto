import os
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.UnidadeFederativa import UnidadeFederativa


os.system("cls || clear")

#Instanciando classe
pessoa1 = Pessoa (135,"jose","13/12/1999","71987845416","josé@gmail.com",Sexo.MASCULINO,Endereco("rua b", "56","predio a","4567841","Salvador",UnidadeFederativa.BAHIA))

print(pessoa1)