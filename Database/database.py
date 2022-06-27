import pickle

def fDBSalvaProprietario(cPropr):
    aPropr = fDbGetProprietarios()
    aPropr.append(cPropr)

    with open(r'Database\dbProprietario.dbx', 'wb') as file:
        pickle.dump(aPropr, file)

def fDBRecuperaProprietarios():
    aPropr = fDbGetProprietarios()
    return aPropr

def fDbGetProprietarios():
    aPropr = []
    try:
        with open(r'Database\dbProprietario.dbx', 'rb') as file:
            aPropr = pickle.load(file)
    except FileNotFoundError as e:
        pass
    return aPropr

def fDbProcuraProprietario(cpf):
    aRes = ['a', 'b', 'c', 'd', 22, 'e', 'f', ]
    #aRes = None
    return aRes