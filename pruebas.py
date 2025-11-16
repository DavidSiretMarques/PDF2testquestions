import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QProgressBar, QPushButton, QVBoxLayout, QFormLayout

# Slot function to handle button click
def on_submit():
    value = progress_bar.value()
    print(f'Progress Bar Value: {value}')

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create a QWidget instance (main window)
window = QWidget()
window.setWindowTitle('Form with QProgressBar Example')
window.setGeometry(100, 100, 400, 300)

# Create a QFormLayout instance
form_layout = QFormLayout()

# Create QLabel and QProgressBar instances
label = QLabel('Task Progress:')
progress_bar = QProgressBar()
progress_bar.setRange(0, 100)  # Set the range of values
progress_bar.setValue(50)      # Set the initial value

# Add widgets to the form layout
form_layout.addRow(label, progress_bar)

# Create a QPushButton for submitting the form
submit_button = QPushButton('Submit')
submit_button.clicked.connect(on_submit)

# Create a QVBoxLayout to combine the form layout and submit button
main_layout = QVBoxLayout()
main_layout.addLayout(form_layout)
main_layout.addWidget(submit_button)

# Set the layout for the main window
window.setLayout(main_layout)

# Show the main window
window.show()

# Run the application's event loop
sys.exit(app.exec())