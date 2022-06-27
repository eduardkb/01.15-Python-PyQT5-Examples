import sys
from Interface.wMain import Ui_MainWindow
from Interface.wProprietarios import Ui_Proprietarios
from Interface.wHelp import Ui_Help
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from PyQt5.Qt import Qt
from PyQt5 import QtGui, QtCore, QtWidgets

from Aplicacao.aplicacao import *

from Interface.Images import Resources


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, aHelpArgs, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.aHelpArgs = aHelpArgs
        self.btnProprietarios.clicked.connect(self.fBtnProprietarios)
        self.btnHelp.clicked.connect(self.fDisplayHelp)
        self.btnListProprietarios.clicked.connect(self.fListarProprietarios)
        self.wProprWindow = None
        self.wHelp = None

        # set Application Icon with Image
        #       scriptDir = os.path.dirname(os.path.realpath(__file__))
        #       self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + r'Images\AppIcon.png'))
        # set Application Icon with resources file
        self.setWindowIcon(QtGui.QIcon(":/Imagens/AppIcon.png"))

        # set image on Help button with Image
        #       self.btnHelp.setIcon(QtGui.QIcon(scriptDir + os.path.sep + r'Images\help.ico'))\
        # set image on Help button with Resources File
        self.btnHelp.setText('')
        self.btnHelp.setIcon(QtGui.QIcon(":/Imagens/Help.ico"))

        self.btnHelp.setIconSize(QtCore.QSize(48, 48))

        self.tableList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

    @staticmethod
    def fStartMainScreen(aHelp):
        qt = QApplication(sys.argv)
        wMain = MainWindow(aHelp)
        wMain.show()
        qt.exec()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F12:
            print("App closed. F12 pressed.")
            self.close()
        if event.key() == Qt.Key_F1:
            self.fDisplayHelp()

    def fDisplayHelp(self):
        if self.wHelp is None:
            self.wHelp = Help(self.aHelpArgs[0], self.aHelpArgs[1], self.aHelpArgs[2], self)
        self.wHelp.show()

    def fBtnProprietarios(self):
        if self.wProprWindow is None:
            self.wProprWindow = ProprietariosWindow(self)
            self.wProprWindow.setWindowModality(Qt.ApplicationModal)
        self.wProprWindow.show()

    def fListarProprietarios(self):
        aListPropr = fAppGetProprietarios()

        numCols = 7
        numLine = len(aListPropr)
        self.tableList.setColumnCount(numCols)
        self.tableList.setRowCount(numLine)
        style = "::section {color: rgb(0, 0, 0);\n" \
                "background-color: rgb(33, 159, 155);\n" \
                "font: 14pt 'MS Shell Dlg 2';}"
        self.tableList.horizontalHeader().setStyleSheet(style)
        self.tableList.setHorizontalHeaderLabels(['CPF', 'RG', 'Nome', 'Sobrenome',
                                                  'Idade', 'Telefone Comercial', 'Telefone Residencial'])

        iRow = 0
        for propr in aListPropr:
            self.tableList.setItem(iRow, 0, QTableWidgetItem(propr.sCpf))
            self.tableList.setItem(iRow, 1, QTableWidgetItem(propr.sRg))
            self.tableList.setItem(iRow, 2, QTableWidgetItem(propr.sNome))
            self.tableList.setItem(iRow, 3, QTableWidgetItem(propr.sSobrenome))
            self.tableList.setItem(iRow, 4, QTableWidgetItem(str(propr.iIdade)))
            self.tableList.setItem(iRow, 5, QTableWidgetItem(propr.sTelefoneCel))
            self.tableList.setItem(iRow, 6, QTableWidgetItem(propr.sTelefoneCom))
            iRow += 1

            self.tableList.resizeColumnsToContents()


class ProprietariosWindow(QMainWindow, Ui_Proprietarios):
    def __init__(self, parent):
        super().__init__(parent)
        super().setupUi(self)

        self.btnSair.clicked.connect(lambda: self.close())
        self.btnLimapr.clicked.connect(self.fBotaoLimpar)
        self.btnSalvar.clicked.connect(self.fSalvaProprietario)
        self.btnProcurar.clicked.connect(self.fProcuraPropr)
        self.statusText.showMessage("Mensagem: ")
        self.statusText.setStyleSheet("border :1px solid black;color: rgb(0, 0, 0);"
                                      "background-color: rgb(200, 200, 200);")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def fBotaoLimpar(self):
        self.fLimparCampos()
        self.statusText.showMessage("Mensagem: Todos os campos limpos.")
        self.statusText.setStyleSheet("border :1px solid black;color: rgb(0, 0, 0);"
                                      "background-color: rgb(200, 200, 200);")

    def fLimparCampos(self):
        self.txtCpf.setText('')
        self.txtRG.setText('')
        self.txtNome.setText('')
        self.txtSobrenome.setText('')
        self.txtIdade.setText('')
        self.txtTelCel.setText('')
        self.txtTelCom.setText('')

    def fSalvaProprietario(self):
        aProp = [self.txtCpf.text(), self.txtRG.text(), self.txtNome.text(), self.txtSobrenome.text(),
                 self.txtIdade.text(), self.txtTelCel.text(), self.txtTelCom.text()]
        bRes = fAppSalvarProprietarios(aProp)
        if bRes == 0:
            self.statusText.showMessage(f"Mensagem: Proprietario {self.txtNome.text()} "
                                        f"de CPF: {self.txtCpf.text()} foi salvo.")
            self.statusText.setStyleSheet("border :1px solid black;color: rgb(0, 0, 0);"
                                          "background-color: rgb(200, 200, 200);")

            self.fLimparCampos()
        else:
            self.statusText.showMessage(f"Mensagem: {bRes}")
            self.statusText.setStyleSheet("border :1px solid black;background-color: rgb(255, 0, 0);"
                                          "color: rgb(255, 255, 255);")

    def fProcuraPropr(self):
        sRes = fAppProcuraProprietario(self.txtCpf.text())
        if sRes is None:
            self.statusText.showMessage(f"Mensagem: Proprietario com CPF '{self.txtCpf.text()}' nao encontrado")
            self.statusText.setStyleSheet("border :1px solid black;background-color: rgb(255, 0, 0);"
                                          "color: rgb(255, 255, 255);")
        else:
            self.txtCpf.setText(sRes[0])
            self.txtRG.setText(sRes[1])
            self.txtNome.setText(sRes[2])
            self.txtSobrenome.setText(sRes[3])
            self.txtIdade.setText(str(sRes[4]))
            self.txtTelCel.setText(sRes[5])
            self.txtTelCel.setText(sRes[6])
            self.statusText.showMessage("Mensagem: Proprietario encontrado e carregado.")
            self.statusText.setStyleSheet("border :1px solid black;color: rgb(0, 0, 0);"
                                          "background-color: rgb(200, 200, 200);")

class Help(QMainWindow, Ui_Help):
    def __init__(self, sDev, sVer, sChangLog, parent):
        super().__init__(parent)
        super().setupUi(self)

        self.txtDeveloper.setText(sDev)
        self.txtVersion.setText(sVer)
        self.txtChangeLog.setText(sChangLog)

        # set image on Help Screen with the image
        #       scriptDir = os.path.dirname(os.path.realpath(__file__))
        #       self.oImagem = QtGui.QPixmap(scriptDir + os.path.sep + r'Images\Lambo.jpg')

        # set image on Help Screen with a Resource File
        self.oImagem = QtGui.QPixmap(":/Imagens/Lambo.jpg")
        self.label_2.setPixmap(self.oImagem)

        # set frameless window
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setStyleSheet("background-color: darkgray;border: 1px solid black")

        self.btnFechar.clicked.connect(lambda: self.close())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
