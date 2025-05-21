import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5 import uic

class Ventana(QMainWindow):
    def __init__(self,texto):
        super().__init__()
        uic.loadUi("Venatana1.ui", self)
        self.btnNombre.clicked.connect(self.imprimirMnesaje)
        self.texto=texto

    def imprimirMnesaje(self):
        self.txtValor.setText(self.texto)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    miventanita = Ventana("Holaaaaaaaaaa ")
    miventanita.show()
    sys.exit(app.exec_())