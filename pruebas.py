import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QWidget, QVBoxLayout, QScrollArea, QLabel, QFrame
)
from PySide6.QtCore import Qt

class DialogoDesplazable(QDialog): # Ahora hereda de QDialog
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ejemplo de QScrollArea en QDialog")
        self.setGeometry(100, 100, 450, 400) # Tamaño inicial del diálogo

        # 1. Crear el Layout Principal del QDialog
        # Este layout será el contenedor del QScrollArea.
        self.main_layout = QVBoxLayout(self)
        
        # 2. Crear el Widget de Contenido (Inner Widget)
        # Este es el widget que contendrá todos los elementos que quieres desplazar.
        self.content_widget = QWidget()
        
        # 3. Crear el Layout para el contenido
        self.content_layout = QVBoxLayout(self.content_widget)
        
        # 4. Añadir mucho contenido al LAYOUT DE CONTENIDO para forzar el scroll
        self.content_layout.addWidget(QLabel("--- INICIO DEL CONTENIDO LARGO EN DIÁLOGO ---"))
        
        for i in range(30): # 30 elementos para asegurar el desplazamiento
            # Etiqueta de texto
            label = QLabel(f"Línea de contenido scrollable #{i + 1}")
            self.content_layout.addWidget(label)
            
            # Separador para claridad
            if (i + 1) % 5 == 0:
                frame = QFrame(frameShape=QFrame.HLine)
                frame.setStyleSheet("background-color: darkblue;")
                self.content_layout.addWidget(frame)

        self.content_layout.addWidget(QLabel("--- FIN DEL CONTENIDO LARGO EN DIÁLOGO ---"))
        
        # 5. Crear el QScrollArea
        self.scroll_area = QScrollArea()
        
        # CLAVE: Asegura que el widget interno se redimensione para llenar el ancho.
        self.scroll_area.setWidgetResizable(True) 

        # 6. Asignar el Widget de Contenido al QScrollArea
        self.scroll_area.setWidget(self.content_widget)
        
        # 7. Añadir el QScrollArea al Layout Principal del QDialog
        # El QScrollArea es el único elemento visible en el diálogo.
        self.main_layout.addWidget(self.scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Crear y mostrar el diálogo
    dialogo = DialogoDesplazable()
    dialogo.show()
    
    # Ejecutar el bucle de eventos de la aplicación
    sys.exit(app.exec())