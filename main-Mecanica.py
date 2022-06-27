from Interface.interface import MainWindow

sVersion = '1.3'
sDeveloper = 'Eduard Keller Buhali'
sChangeLog = """    » 1.0 - Start first screen
    » 1.1 - Help Screen
    » 1.2 - Proprietários Screen
    » 1.3 - Proprietários Inteligence
    
Future Improvements:
    » aplicaçao fAppSalvarProprietarios --> tratar campos
    » aplicacao fTrataString --> remover espaços de mais no meio da string
    » database fDBSalvaProprietario --> tratar cpf duplicado
    » interface fListarProprietarios --> distribuir tamanho das colunas
"""
sSep = '######################'
sHelpStr = f'{sSep}\nDeveloper: {sDeveloper}\nVersion: {sVersion}\n' \
            f'{sSep}\nChangelog:\n{sChangeLog}'
aHelp = [sDeveloper, sVersion, sChangeLog]
print(sHelpStr)
print("##########################################################")
# start application:
MainWindow.fStartMainScreen(aHelp)

