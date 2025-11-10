import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QSplitter,
    QVBoxLayout, QHBoxLayout, QLabel, QListWidget,
    QPushButton, QRadioButton, QSizePolicy
)
from PySide6.QtCore import Qt

# --- Datos de ejemplo (Simulación) ---
# En un proyecto real, cargarías esto desde una base de datos o un archivo.
EJEMPLO_PREGUNTAS = [
    {
        "titulo": "Pregunta 1: Introducción a Python",
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": ["class", "def", "func", "void"],
        "referencia": "Referencia: Documentación oficial de Python."
    },
    {
        "titulo": "Pregunta 2: POO",
        "pregunta": "¿Qué concepto describe la ocultación de datos y la implementación?",
        "opciones": ["Herencia", "Polimorfismo", "Abstracción", "Encapsulación"],
        "referencia": "Referencia: Principios SOLID."
    },
    {
        "titulo": "Pregunta 3: PySide 6",
        "pregunta": "¿Cuál es el módulo principal para los widgets de PySide 6?",
        "opciones": ["QtGui", "QtCore", "QtWidgets", "QtNetwork"],
        "referencia": "Referencia: Módulos de PySide 6."
    }
]

class TestSimu(QMainWindow):
    """
    Clase principal para la simulación de examen.
    """
    def __init__(self, preguntas):
        super().__init__()
        self.setWindowTitle("Simulador de Examen - PySide 6")
        self.setGeometry(100, 100, 800, 600)  # 

        self.preguntas = preguntas
        self.indice_actual = 0

        # --- Widget Central Contenedor ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Diseño principal (Horizontal: Lista | Contenido)
        main_layout = QHBoxLayout(central_widget)
        
        # QSplitter permite redimensionar los paneles arrastrando
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter)

        # 1. Panel Izquierdo: Lista de Preguntas
        self._crear_panel_lista(splitter)

        # 2. Panel Derecho: Contenido de la Pregunta
        self._crear_panel_contenido(splitter)

        # Establecer tamaños iniciales del splitter (ej. 1/4 para la lista, 3/4 para el contenido)
        splitter.setSizes([200, 600])

        # Inicializar la visualización de la primera pregunta
        self._cargar_pregunta(self.indice_actual)

    def _crear_panel_lista(self, parent_splitter):
        """Crea y configura el QListWidget para la navegación."""
        self.lista_preguntas = QListWidget()
        self.lista_preguntas.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        parent_splitter.addWidget(self.lista_preguntas)

        # Llenar la lista con los títulos
        for i, pregunta in enumerate(self.preguntas):
            self.lista_preguntas.addItem(f"{i+1}. {pregunta['titulo']}")

        # Conectar el clic de la lista al método de navegación
        self.lista_preguntas.currentRowChanged.connect(self._navegar_por_lista)

    def _crear_panel_contenido(self, parent_splitter):
        """Crea el contenedor para la pregunta, opciones y botones."""
        contenido_widget = QWidget()
        layout_contenido = QVBoxLayout(contenido_widget)
        
        # --- Área Superior: Pregunta y Opciones (Scrolleable) ---
        self.area_pregunta = QWidget()
        self.layout_pregunta_opciones = QVBoxLayout(self.area_pregunta)
        # Aquí se actualizarán los QLabel y QRadioButton

        # Contenedor para la referencia
        self.label_referencia = QLabel("Referencia Placeholder")
        self.label_referencia.setStyleSheet("font-style: italic; color: gray;")
        self.label_referencia.setWordWrap(True)

        # Separador visual (QHLine es más limpio que QFrame en este caso)
        separador = QWidget()
        separador.setFixedHeight(1)
        separador.setStyleSheet("background-color: lightgray;")
        
        layout_contenido.addWidget(self.area_pregunta)
        layout_contenido.addWidget(separador) # HLine
        layout_contenido.addWidget(self.label_referencia)
        layout_contenido.addStretch(1) # Empuja la referencia y la línea hacia arriba
        
        # --- Área Inferior: Botones ---
        layout_botones = QHBoxLayout()
        self.btn_anterior = QPushButton("Anterior")
        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_finalizar = QPushButton("Finalizar Examen")

        # Conectar botones a sus métodos
        self.btn_anterior.clicked.connect(self._anterior_pregunta)
        self.btn_siguiente.clicked.connect(self._siguiente_pregunta)
        self.btn_finalizar.clicked.connect(self._finalizar_examen)

        layout_botones.addWidget(self.btn_anterior)
        layout_botones.addStretch(1) # Espacio flexible
        layout_botones.addWidget(self.btn_siguiente)
        layout_botones.addWidget(self.btn_finalizar)

        layout_contenido.addLayout(layout_botones)
        
        parent_splitter.addWidget(contenido_widget)
        
    def _limpiar_layout(self, layout):
        """Función auxiliar para limpiar los widgets de un layout."""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def _cargar_pregunta(self, indice):
        """Actualiza el panel de contenido con los datos de la pregunta en el índice dado."""
        if not 0 <= indice < len(self.preguntas):
            return

        self.indice_actual = indice
        pregunta_data = self.preguntas[indice]
        
        # Actualizar la selección en la lista
        self.lista_preguntas.setCurrentRow(indice)
        
        # Limpiar widgets anteriores
        self._limpiar_layout(self.layout_pregunta_opciones)
        
        # 1. Título/Pregunta
        label_pregunta = QLabel(f"**{pregunta_data['pregunta']}**")
        label_pregunta.setWordWrap(True)
        self.layout_pregunta_opciones.addWidget(label_pregunta)
        
        # 2. Opciones
        # Creamos un GroupBox o un QWidget simple para agrupar las opciones
        opciones_widget = QWidget()
        layout_opciones = QVBoxLayout(opciones_widget)
        layout_opciones.setContentsMargins(10, 10, 10, 10) # Pequeño margen
        
        for opcion in pregunta_data["opciones"]:
            radio_btn = QRadioButton(opcion)
            #radio_btn.setWordWrap(True)
            layout_opciones.addWidget(radio_btn)
        
        self.layout_pregunta_opciones.addWidget(opciones_widget)
        self.layout_pregunta_opciones.addStretch(1) # Relleno vertical
        
        # 3. Referencia
        self.label_referencia.setText(pregunta_data["referencia"])

        # 4. Actualizar estado de los botones (desactivar si es el principio/fin)
        self.btn_anterior.setEnabled(self.indice_actual > 0)
        self.btn_siguiente.setEnabled(self.indice_actual < len(self.preguntas) - 1)

    # --- Métodos de Navegación ---
    def _navegar_por_lista(self, fila):
        """Maneja la navegación al hacer clic en un elemento de la lista."""
        self._cargar_pregunta(fila)

    def _anterior_pregunta(self):
        """Va a la pregunta anterior si existe."""
        if self.indice_actual > 0:
            self._cargar_pregunta(self.indice_actual - 1)

    def _siguiente_pregunta(self):
        """Va a la siguiente pregunta si existe."""
        if self.indice_actual < len(self.preguntas) - 1:
            self._cargar_pregunta(self.indice_actual + 1)
            
    def _finalizar_examen(self):
        """Maneja el evento de finalizar el examen."""
        # Aquí iría la lógica para calcular la puntuación, guardar resultados, etc.
        print("--- Examen Finalizado ---")
        # Mostrar un diálogo o cerrar la ventana, por ejemplo:
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TestSimu(EJEMPLO_PREGUNTAS)
    ventana.show()
    sys.exit(app.exec())