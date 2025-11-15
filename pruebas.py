import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QRadioButton, QGroupBox, QSizePolicy, 
    QLabel
)
from PySide6.QtCore import Qt, Signal

# --- CLASE PERSONALIZADA ---
class ClickableLabel(QLabel):
    """QLabel que emite una señal al ser clickeada."""
    clicked = Signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)
# ----------------------------------------------------
class QRadioButtonW(QRadioButton):
    pass

class ManualConnectDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo de Clic Manual para RadioButton (Corregido)")
        self.setGeometry(200, 200, 550, 200)
        
        main_layout = QVBoxLayout(self)
        
        grupo = QGroupBox("Opciones con Conexión Manual de Eventos")
        grupo_layout = QVBoxLayout(grupo)
        
        # --- Creación de la Fila (La Solución Funcional) ---
        
        fila_layout = QHBoxLayout()
        fila_layout.setSpacing(0) 
        
        self.radio_btn = QRadioButton()
        
        # Usar nuestra ClickableLabel personalizada
        self.etiqueta_clickeable = ClickableLabel("Opción 1: ¡Haz clic aquí! (Conexión Manual)")
        self.etiqueta_clickeable.setWordWrap(True)
        
        # Retroalimentación visual
        self.etiqueta_clickeable.setCursor(Qt.PointingHandCursor)
        
        # CONECTAR la señal 'clicked' de la etiqueta al método 'click' del botón
        self.etiqueta_clickeable.clicked.connect(self.radio_btn.click)
        
        # 3. Añadir al layout horizontal
        fila_layout.addWidget(self.radio_btn)
        fila_layout.addWidget(self.etiqueta_clickeable)
        fila_layout.addStretch()
        
        grupo_layout.addLayout(fila_layout)
        
        # --- Fila 2 (Normal) ---
        
        fila_layout_normal = QHBoxLayout()
        fila_layout_normal.addWidget(QRadioButton())
        fila_layout_normal.addWidget(QLabel("Opción 2: Solo funciona el clic en el círculo (Comparación)", wordWrap=True))
        fila_layout_normal.addStretch()
        grupo_layout.addLayout(fila_layout_normal)

        main_layout.addWidget(grupo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManualConnectDemo()
    window.show()
    sys.exit(app.exec())