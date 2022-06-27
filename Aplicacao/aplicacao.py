import re
from Aplicacao.classes import Proprietarios
from Database.database import *

def fAppSalvarProprietarios(aProp):
    sCpf = fTrataString(aProp[0])
    sRg = fTrataString(aProp[1])
    sNome = fTrataString(aProp[2])
    sSobrenome = fTrataString(aProp[3])
    iIdade = fTrataInt(aProp[4])
    sTelCel = fTrataString(aProp[5])
    sTelCom = fTrataString(aProp[6])

    if len(sCpf) < 3:
        return 'CPF Inválido'
    if len(sRg) < 3:
        return 'RG Inválido'
    if len(sNome) < 3:
        return 'Nome Inválido (Precisa ter mais de 3 letras)'
    if len(sSobrenome) < 3:
        return 'Sobrenome Inválido (Precisa ter mais de 3 letras)'
    if iIdade < 18 or iIdade > 120:
        return 'Idade precisa estar emtre 18 e 120 anos'
    if len(sTelCel) < 3:
        return 'Telefone Celular precisa ter mais digitios.'

    propr = Proprietarios(sCpf, sRg, sNome, sSobrenome, iIdade, sTelCel, sTelCom)
    fDBSalvaProprietario(propr)
    return 0

def fAppGetProprietarios():
    return fDBRecuperaProprietarios()

def fTrataString(sText):
    sText = sText.strip()
    return sText

def fTrataInt(sText):
    iRes = re.sub(r'[^0-9]', '', sText)
    try:
        return int(iRes)
    except Exception:
        return 0

def fAppProcuraProprietario(cpf):
    return fDbProcuraProprietario(cpf)


