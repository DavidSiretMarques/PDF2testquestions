import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (QWidget, QMenuBar, QMenu, QGroupBox, QHBoxLayout, QRadioButton,
                               QPushButton, QLabel, QVBoxLayout, QGridLayout, QApplication, QFrame,
                               QStackedLayout, QDialog, QScrollArea)

class TestSimu(QWidget):
    def __init__(self, questions):
        super().__init__()
        self.setWindowTitle("Simulacro")
        self.setWindowIcon(QtGui.QIcon('exam.ico'))
        self.questions = questions
        #self.current_question_index = 0

        #Set question and button layout
        self.create_questions()
        self.create_button_group()

        #Add everything to layout
        self.layout = QGridLayout(self)
        self.layout.addLayout(self._question_layout,0,1)
        self.layout.addWidget(self._button_group_box,1,1)

        #Set button actions
        self.buttonnext.clicked.connect(self.next_question)
        self.buttonprev.clicked.connect(self.prev_question)
        self.buttonfin.clicked.connect(self.end_test)

    @QtCore.Slot()
    def end_test(self):
        notice = QDialog()
        notice.setWindowTitle("Corrección")
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_widget.setLayout(content_layout)
        title_label = QLabel("Corrección de las preguntas.")
        content_layout.addWidget(title_label)
        for i,question in enumerate(self.questions):
            question_group = QGroupBox()
            question_layout = QVBoxLayout()
            question_group.setLayout(question_layout)
            #Iteratively create question and options
            question_layout.addWidget(QLabel(question['pregunta'], wordWrap=True))
            option_button = ["a)","b)","c)","d)"] #Hardcoded for 4 options
            for  j,option in enumerate(question['opciones']):
                opt_button = QRadioButton(option_button[j], enabled=False, checked=True if self._question_layout.widget(i).findChildren(QRadioButton)[j].isChecked()==True else False)
                opt_label = QLabel(option, wordWrap=True, )
                if opt_label.text() == question['respuesta']:
                    opt_label.setStyleSheet("background-color: green;")
                    opt_button.setStyleSheet("background-color: green;")
                else:
                    opt_button.setStyleSheet("background-color: red;")
                    opt_label.setStyleSheet("background-color: red;")
                ly = QHBoxLayout()
                ly.addWidget(opt_button,1)
                ly.addWidget(opt_label,10)
                question_layout.addLayout(ly)

            question_layout.addWidget(QFrame(frameShape=QFrame.HLine))
            question_layout.addWidget(QLabel(f"Referencia: {question['reference']}", wordWrap=True))
            content_layout.addWidget(question_group)
            print(f'Question Added {i}')

        #Make scrollable
        scroll_Area = QScrollArea()
        scroll_Area.setWidgetResizable(True)
        scroll_Area.setWidget(content_widget)
        main_layout = QVBoxLayout(notice)
        main_layout.addWidget(scroll_Area)

        #Show and execute)
        notice.show()
        notice.exec()

    @QtCore.Slot()
    def next_question(self):
        if self._question_layout.currentIndex() < len(self.questions) - 1:
            self._question_layout.setCurrentIndex(self._question_layout.currentIndex() + 1)
        else:
            notice = QDialog()
            notice.setWindowTitle("Aviso")
            notice_layout = QVBoxLayout()
            notice.setLayout(notice_layout)
            notice_label = QLabel("Ha llegado a la última pregunta.")
            notice_layout.addWidget(notice_label)
            notice.resize(200,100)
            notice.exec()

    @QtCore.Slot()
    def prev_question(self):
        if self._question_layout.currentIndex() > 0:
            self._question_layout.setCurrentIndex(self._question_layout.currentIndex() - 1)
        else:
            notice = QDialog()
            notice.setWindowTitle("Aviso")
            notice_layout = QVBoxLayout()
            notice.setLayout(notice_layout)
            notice_label = QLabel("Ha llegado a la primera pregunta.")
            notice_layout.addWidget(notice_label)
            notice.resize(200,100)
            notice.exec()

    def create_menu(self): #WIP
        self._menu_bar = QMenuBar()

        self._file_menu = QMenu("&File", self)
        self._exit_action = self._file_menu.addAction("&Exit")
        self._menu_bar.addMenu(self._file_menu)

        self._exit_action.triggered.connect(self.accept)

    def create_questions(self):
        #Set Question layout
        self._question_layout = QStackedLayout()
        opciones = ["a)","b)","c)","d)"] #Hardcoded for 4 options
        #Iteratively create question and options
        for question in self.questions:
            question_group = QGroupBox()
            question_layout = QVBoxLayout()
            question_group.setLayout(question_layout)
            question_layout.addWidget(QLabel(question['pregunta'], wordWrap=True))
            #Create options
            for j,option in enumerate(question['opciones']):
                opt_button = QRadioButton(opciones[j])
                opt_label = QLabel(option, wordWrap=True)
                ly = QHBoxLayout()
                ly.setSpacing(0)
                ly.addWidget(opt_button,1)
                ly.addWidget(opt_label,10)
                question_layout.addLayout(ly)
            question_layout.addWidget(QFrame(frameShape=QFrame.HLine))
            question_layout.addWidget(QLabel("Referencia:", wordWrap=True))
            self._question_layout.addWidget(question_group)

    def create_button_group(self):

        #create control buttons
        self.buttonprev = QPushButton("Anterior")
        self.buttonnext = QPushButton("Siguiente")
        self.buttonfin = QPushButton("Finalizar")

        #Create button layout
        self._button_group_box = QGroupBox(flat=True)
        layout = QHBoxLayout()

        self._button_group_box.setLayout(layout)
        layout.addWidget(self.buttonprev)
        layout.addWidget(self.buttonnext)
        layout.addWidget(self.buttonfin)


if __name__ == "__main__":

    qs = [
    {
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
    },
    {
        "pregunta": "El Reglamento de Instalaciones de Protección Contra Incendios se aplicará con carácter supletorio, con una excepción específica. ¿Cuál es esta excepción?",
        "opciones": [
            "Las instalaciones de protección activa contra incendios en edificios de uso residencial vivienda.",
            "Los túneles de carreteras del Estado, cuya regulación en materia de seguridad se regirá por el Real Decreto 635/2006.",
            "Los sistemas de detección y alarma de incendios en zonas urbanas.",
            "Los equipos de protección activa contra incendios sujetos al marcado CE."
        ],
        "respuesta": "Los túneles de carreteras del Estado, cuya regulación en materia de seguridad se regirá por el Real Decreto 635/2006.",
        "tema": "Ámbito de aplicación supletorio",
        "dificultad": 2,
        "creation_date": "5/11/2025",
        "reference": "Artículo 1.2. Asimismo, el presente Reglamento se aplicará con carácter supletorio en aquellos aspectos relacionados con las instalaciones de protección activa contra incendios no regulados en las legislaciones específicas, con la excepción de los túneles de carreteras del Estado, cuya regulación en materia de seguridad se regirá por el Real Decreto 635/2006, de 26 de mayo, sobre requisitos mínimos de seguridad en los túneles de carreteras del Estado."
    },
    {
        "pregunta": "Según el Reglamento de Instalaciones de Protección Contra Incendios, ¿quiénes están sujetos a sus disposiciones?",
        "opciones": [
            "Solo las empresas instaladoras de sistemas de protección activa contra incendios.",
            "Solo las empresas mantenedoras de instalaciones de protección contra incendios.",
            "Las empresas instaladoras y mantenedoras, así como fabricantes, importadores, distribuidores u organismos que intervengan en la certificación o evaluación técnica de los productos.",
            "Únicamente los usuarios finales de las instalaciones de protección contra incendios."
        ],
        "respuesta": "Las empresas instaladoras y mantenedoras, así como fabricantes, importadores, distribuidores u organismos que intervengan en la certificación o evaluación técnica de los productos.",
        "tema": "Ámbito de aplicación subjetivo",
        "dificultad": 2,
        "creation_date": "5/11/2025",
        "reference": "Artículo 2. Ámbito de aplicación subjetivo. 1. Estarán sujetos a las disposiciones de este Reglamento tanto las empresas instaladoras como las empresas mantenedoras de instalaciones de protección contra incendios. 2. Asimismo, las exigencias técnicas de este Reglamento se aplicarán a los fabricantes, importadores, distribuidores u organismos que intervengan en la certificación o evaluación técnica de los productos, y a todos aquellos que pudieran verse afectados por esta regulación."
    },
    {
        "pregunta": "De acuerdo con el Artículo 3 del Reglamento de Instalaciones de Protección Contra Incendios, ¿qué se entiende por 'Protección activa contra incendios'?",
        "opciones": [
            "El conjunto de medidas pasivas para prevenir la propagación del fuego.",
            "El conjunto de medios, equipos y sistemas, ya sean manuales o automáticos, cuyas funciones específicas son la detección, control y/o extinción de un incendio, facilitando la evacuación de los ocupantes e impidiendo que el incendio se propague, minimizando así las pérdidas personales y materiales.",
            "Los productos y materiales de construcción que retardan la acción del fuego.",
            "El sistema de evacuación de humos y calor diseñado para la seguridad de las personas."
        ],
        "respuesta": "El conjunto de medios, equipos y sistemas, ya sean manuales o automáticos, cuyas funciones específicas son la detección, control y/o extinción de un incendio, facilitando la evacuación de los ocupantes e impidiendo que el incendio se propague, minimizando así las pérdidas personales y materiales.",
        "tema": "Definiciones",
        "dificultad": 1,
        "creation_date": "5/11/2025",
        "reference": "Artículo 3. Definiciones. a) Protección activa contra incendios: es el conjunto de medios, equipos y sistemas, ya sean manuales o automáticos, cuyas funciones específicas son la detección, control y/o extinción de un incendio, facilitando la evacuación de los ocupantes e impidiendo que el incendio se propague, minimizando así las pérdidas personales y materiales."
    },
    {
        "pregunta": "Según el Anexo I del Reglamento de Instalaciones de Protección Contra Incendios, ¿cuál es la masa máxima de un extintor portátil en condiciones de funcionamiento?",
        "opciones": [
            "Superior a 20 kg.",
            "Igual o inferior a 15 kg.",
            "Igual o inferior a 20 kg.",
            "Cualquier masa, siempre que pueda ser transportado a mano."
        ],
        "respuesta": "Igual o inferior a 20 kg.",
        "tema": "Extintores de incendio",
        "dificultad": 1,
        "creation_date": "5/11/2025",
        "reference": "ANEXO I. Sección 1.ª Protección activa contra incendios. 4. Extintores de incendio. 1. En función de la carga, los extintores se clasifican de la siguiente forma: a) Extintor portátil: Diseñado para que puedan ser llevados y utilizados a mano, teniendo en condiciones de funcionamiento una masa igual o inferior a 20 kg."
    }
]
    app = QApplication([])

    widget = TestSimu(qs)
    widget.resize(600, 600)
    widget.show()

    sys.exit(app.exec())
