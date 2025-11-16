import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (QWidget, QGroupBox, QHBoxLayout, QRadioButton,
                               QPushButton, QLabel, QVBoxLayout, QGridLayout, QApplication, QFrame,
                               QStackedLayout, QDialog)


class TestRev(QWidget):
    def __init__(self, questions):
        """Initializes the question review window with provided questions."""
        super().__init__()
        self.setWindowTitle("Revisión de preguntas")
        self.setWindowIcon(QtGui.QIcon('working.ico'))
        self.questions = questions
        self.answered_questions = 0
        self._progress_label = QLabel(f'{self.answered_questions}/{len(self.questions)} Respondidas')

        #Set question list, question and button layout
        self._create_questions()
        self._create_button_group()

        #Add everything to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self._progress_label, 0, 0)
        self.layout.addLayout(self._question_layout,0,1)
        self.layout.addWidget(self._button_group_box,1,1)

        #Set button actions
        self.buttonnext.clicked.connect(self._next_question)
        self.buttonprev.clicked.connect(self._prev_question)
        self.buttonfin.clicked.connect(self.close)

    def _create_questions(self):
        """Creates the question layout, setting question, options and reference"""
        #Set Question layout
        self._question_layout = QStackedLayout()
        #Iteratively create question and options
        for question in self.questions:
            question_group = QGroupBox()
            question_layout = QVBoxLayout()
            question_group.setLayout(question_layout)
            question_layout.addWidget(QLabel(question['pregunta'], wordWrap=True))
            #[question_layout.addWidget(QRadioButton(opcion)) for opcion in question['opciones']]
            for opcion in question['opciones']:
                radiobutton = QRadioButton(opcion)
                radiobutton.clicked.connect(self._update_progress)
                question_layout.addWidget(radiobutton)
            question_layout.addWidget(QFrame(frameShape=QFrame.HLine))
            question_layout.addWidget(QLabel("Referencia:", wordWrap=True))
            cleanbutton = QPushButton("Limpiar Pregunta")
            question_layout.addWidget(cleanbutton)
            cleanbutton.clicked.connect(self._clean_question)
            self._question_layout.addWidget(question_group)

    def _create_button_group(self):
        """Creates the control buttons and sets their actions"""
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

    # Navigation Methods
    @QtCore.Slot()
    def _prev_question(self):
        """Moves to the previous question in the layout. If there are no previous questions, shows a notice."""
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

    @QtCore.Slot()
    def _next_question(self):
        """Moves to the next question in the layout. If there are no more questions, shows a notice."""
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

    #Checking and cleaning methods
    @QtCore.Slot()
    def _clean_question(self):
        """Cleans selected option in the question to make it unanswered"""
        for option in self._question_layout.currentWidget().findChildren(QRadioButton):
            if option.isChecked():
                option.setAutoExclusive(False)
                option.setChecked(False)
                option.setAutoExclusive(True)
                self._update_progress(-1)

    @QtCore.Slot()
    def _update_progress(self, progress):
        """Set the label to show the number of answered questions"""
        self.answered_questions += progress
        self._progress_label.setText(f'{self.answered_questions}/{len(self.questions)} Respondidas')

if __name__ == "__main__":
    qs = [
    {
        "pregunta": "Question1",
        "opciones": [
            "Option1.",
            "Option2.",
            "Option3.",
            "Option4."
        ],
        "respuesta": "Option2.",
        "tema": "Subject1",
        "dificultad": 1,
        "creation_date": "5/11/2025",
        "reference": "Reference1."
    },
    {
        "pregunta": "Question2",
        "opciones": [
            "Option1.",
            "Option2.",
            "Option3.",
            "Option4."
        ],
        "respuesta": "Option3.",
        "tema": "Subject1",
        "dificultad": 1,
        "creation_date": "5/11/2025",
        "reference": "Reference2."
    }
   ]
    app = QApplication([])

    widget = TestRev(qs)
    widget.resize(600, 600)
    widget.show()

    sys.exit(app.exec())
