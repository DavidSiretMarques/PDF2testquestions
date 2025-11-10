from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QGroupBox, QRadioButton, QFrame, QScrollArea, QWidget
)
from PySide6.QtCore import Qt # Importar Qt para QFrame.HLine y QScrollArea

# Supongamos que 'self.questions' y '_question_layout' existen en el scope de la función/método
# (He comentado las líneas que dependen de variables externas para que el ejemplo corra sin errores,
# pero he mantenido la estructura de tu lógica.)
app = QApplication([])

widget = notice()
widget.resize(600, 600)
widget.show()

    sys.exit(app.exec())
# --- Inicio de la corrección del código ---
notice = QDialog()
notice.setWindowTitle("Corrección")

# 1. Crear el Widget de Contenido (Inner Widget)
# Este widget contendrá todos los elementos desplazables
content_widget = QWidget()
content_layout = QVBoxLayout(content_widget)

# Asignar el layout al widget de contenido
content_widget.setLayout(content_layout)

# Añadir el label principal al widget de contenido
notice_label = QLabel("Corrección de las preguntas.")
content_layout.addWidget(notice_label)

# -------------------------------------------------------------
# Bucle para añadir preguntas y opciones (Mantenemos tu lógica)
# -------------------------------------------------------------
# for i,question in enumerate(self.questions):
#     question_group = QGroupBox()
#     question_layout = QVBoxLayout()
#     question_group.setLayout(question_layout)
    
#     # Añadir pregunta
#     question_layout.addWidget(QLabel(question['pregunta'], wordWrap=True))
    
#     # Añadir opciones
#     for j,option in enumerate(question['opciones']):
#         # Optimizando la creación del QRadioButton para el ejemplo
#         # is_checked = self._question_layout.widget(i).findChildren(QRadioButton)[j].isChecked()
#         is_checked = False # Usamos un valor por defecto para el ejemplo
#         opt_button = QRadioButton(option, enabled=False, checked=is_checked)
        
#         if opt_button.text() == question['respuesta']:
#             opt_button.setStyleSheet("color: green;")
#         else:
#             opt_button.setStyleSheet("color: red;")
            
#         question_layout.addWidget(opt_button)
        
#     question_layout.addWidget(QFrame(frameShape=QFrame.HLine))
#     question_layout.addWidget(QLabel(f"Referencia: {question['reference']}", wordWrap=True))
    
#     # 2. Añadir el grupo de preguntas al LAYOUT DEL WIDGET DE CONTENIDO
#     content_layout.addWidget(question_group)
#     # print(f'Question Added {i}')
    
# Código de ejemplo para simular contenido largo:
for i in range(15):
    content_layout.addWidget(QLabel(f"Pregunta de Ejemplo #{i+1} con corrección."))
    group = QGroupBox()
    group.setLayout(QVBoxLayout())
    group.layout().addWidget(QLabel("Opción correcta: Verde"))
    content_layout.addWidget(group)
# Aseguramos que el contenido ocupe el espacio necesario
content_layout.addStretch() 
# -------------------------------------------------------------
# FIN del Bucle
# -------------------------------------------------------------

# 3. Crear el QScrollArea y establecer el Widget de Contenido
scroll_area = QScrollArea()
# Hace que el widget de contenido se ajuste horizontalmente, 
# pero permite el scroll vertical si el contenido es muy alto.
scroll_area.setWidgetResizable(True) 
# El widget que contiene todo el contenido se establece como el widget de la scroll area
scroll_area.setWidget(content_widget)


# 4. Establecer el layout principal de QDialog y añadir el QScrollArea
# Este es el paso final que hace que la QDialog use el scroll.
notice_main_layout = QVBoxLayout(notice)
notice_main_layout.addWidget(scroll_area)
notice.setLayout(notice_main_layout)

# El QDialog está listo para mostrarse
notice.show()
notice.exec()