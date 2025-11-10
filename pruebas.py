import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel
)
from PySide6.QtCore import Qt

class EspaciadoMinimoDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Espaciado Mínimo entre Widgets")
        self.setGeometry(100, 100, 400, 150)
        
        # Layout Vertical principal
        main_layout = QVBoxLayout(self)
        
        # --- 1. Espaciado por Defecto para Comparación ---
        self.layout_separado = QHBoxLayout()
        self.layout_separado.addWidget(QRadioButton('asdf'))
        self.layout_separado.addWidget(QLabel("Opción 1: Espaciado Normal"))
        self.layout_separado.addStretch() # Empuja los widgets a la izquierda
        main_layout.addLayout(self.layout_separado)
        
        # --- 2. Espaciado Mínimo (Solución) ---
        self.layout_junto = QHBoxLayout()
        
        # 🟢 CLAVE: Establecer el espaciado del layout a 0
        self.layout_junto.setSpacing(0) 
        
        # ⚠️ Nota: También puedes usar setContentsMargins(0, 0, 0, 0) en el layout,
        # aunque setSpacing(0) suele ser suficiente para el espacio entre widgets.
        
        self.layout_junto.addWidget(QRadioButton('asdf'))
        self.layout_junto.addWidget(QLabel("Opción 2: Espaciado Mínimo (Junto)"))
        self.layout_junto.addStretch()
        
        main_layout.addLayout(self.layout_junto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EspaciadoMinimoDemo()
    window.show()
    sys.exit(app.exec())