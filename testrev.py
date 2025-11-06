import sys
import random
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QWidget, QMenuBar, QMenu, QGroupBox, QHBoxLayout, QRadioButton, QPushButton, QLabel, QVBoxLayout, QApplication

class TestRev(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Revisión de preguntas")
        self.setWindowIcon(QtGui.QIcon('working.ico'))
        self.options = [QRadioButton(opcion) for opcion in question['opciones']]
        #create control buttons
        self.buttonprev = QPushButton("Anterior")
        self.buttonnext = QPushButton("Siguiente")
        self.buttoncorr = QPushButton("Corregir")
        self.buttonfin = QPushButton("Finalizar")
        self.buttonsave = QPushButton("Guardar pregunta")
        self.buttondel = QPushButton("Eliminar pregunta")
        self.text = QLabel(question['pregunta'], alignment=QtCore.Qt.AlignTop)
        
        #Set button layout
        self.create_button_group_box()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        for option in self.options:
            self.layout.addWidget(option)
        self.layout.addWidget(self._button_group_box)
        
        self.buttoncorr.clicked.connect(self.corregir)
        self.buttonfin.clicked.connect(self.close)

    @QtCore.Slot()
    def corregir(self):
        for option in self.options:
            if option.isChecked():
                if option.text() == question['respuesta']:
                    self.options = [option.setStyleSheet("color: green;") for option in self.options]
                else:
                    self.options = [option.setStyleSheet("color: red;") for option in self.options]
                    
    def create_menu(self):
        self._menu_bar = QMenuBar()

        self._file_menu = QMenu("&File", self)
        self._exit_action = self._file_menu.addAction("E&xit")
        self._menu_bar.addMenu(self._file_menu)

        self._exit_action.triggered.connect(self.accept)
        
    def create_button_group_box(self):
        self._button_group_box = QGroupBox(flat=True)
        layout = QHBoxLayout()

        self._button_group_box.setLayout(layout)
        layout.addWidget(self.buttonprev)
        layout.addWidget(self.buttonnext)
        layout.addWidget(self.buttoncorr)
        layout.addWidget(self.buttonfin)
        layout.addWidget(self.buttonsave)
        layout.addWidget(self.buttondel)
        
if __name__ == "__main__":
    question = {
        "pregunta": "Según el Reglamento de Instalaciones de Protección Contra Incendios, ¿cuál es el objeto principal de este Reglamento?",
        "opciones": [
            "La regulación de la seguridad en túneles de carreteras del Estado.",
            "La determinación de las condiciones y requisitos exigibles al diseño, instalación, mantenimiento e inspección de los equipos y sistemas de protección activa contra incendios.",
            "El establecimiento de las normativas para la fabricación de extintores portátiles.",
            "La inspección de sistemas de protección pasiva contra incendios."
        ],
        "respuesta": "La determinación de las condiciones y requisitos exigibles al diseño, instalación, mantenimiento e inspección de los equipos y sistemas de protección activa contra incendios.",
        "tema": "Objeto del Reglamento",
        "dificultad": 1,
        "creation_date": "5/11/2025",
        "reference": "Artículo 1. Objeto y ámbito de aplicación material. 1. Constituye el objeto de este Reglamento la determinación de las condiciones y los requisitos exigibles al diseño, instalación/aplicación, mantenimiento e inspección de los equipos, sistemas y componentes que conforman las instalaciones de protección activa contra incendios."
    }
    app = QApplication([])

    widget = TestRev()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())