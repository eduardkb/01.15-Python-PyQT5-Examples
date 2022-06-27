import sys
from validaCPF import fValidaCPF, fFormataCPF
from geradorCPF import fGeraCPF
from Interface.mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

print('CPF Gerado 1:', fGeraCPF())
print('CPF Gerado 2:', fFormataCPF(fGeraCPF()))

class GeraCPFInterface(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.fGeraCPF)
        self.btnValidaCPF.clicked.connect(self.fValidaCpf)

    def fGeraCPF(self):
        self.labelRetorno.setText(f'CPF Gerado: {str(fFormataCPF(fGeraCPF()))}')

    def fValidaCpf(self):
        cpf = self.inputValidaCPF.text()
        bCPFValido = fValidaCPF(cpf)
        # if len(cpf) == 11:
        #     cpf = fFormataCPF(cpf)
        if bCPFValido:
            self.labelRetorno.setText(f'CPF Válido: {fFormataCPF(cpf)}')
        else:
            self.labelRetorno.setText(f'O CPF "{fFormataCPF(cpf)}" é inválido!')

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    cGeraCPF = GeraCPFInterface()
    cGeraCPF.show()
    qt.exec_()
