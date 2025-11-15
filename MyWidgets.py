from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QRadioButton

class WrappedRadioButton(QWidget):
    """A radio button with word-wrapped text label"""
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        self.radio_button = QRadioButton()
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setBuddy(self.radio_button)

        layout.addWidget(self.radio_button, 0)
        layout.addWidget(self.label, 1)

    def isChecked(self):
        """Getter of property checked"""
        return self.radio_button.isChecked()

    def setChecked(self, checked):
        """Setter of property checked"""
        self.radio_button.setChecked(checked)
