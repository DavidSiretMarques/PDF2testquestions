import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QSplitter,
    QVBoxLayout, QHBoxLayout, QLabel, QListWidget,
    QPushButton, QRadioButton, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6 import QtCore

# --- Datos de ejemplo (Simulación) ---
# En un proyecto real, cargarías esto desde una base de datos o un archivo.
EJEMPLO_PREGUNTAS = [
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
    
class TestSimu(QMainWindow):
    """
    Clase principal para la simulación de examen.
    """
    def __init__(self, preguntas):
        super().__init__()
        self.setWindowTitle("Simulador de Examen - PySide 6")

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

        # Inicializar la visualización de la primera pregunta
        self._cargar_pregunta(self.indice_actual)

    def _crear_panel_lista(self, parent_splitter):
        """Crea y configura el QListWidget para la navegación."""
        self.lista_preguntas = QListWidget()
        self.lista_preguntas.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        parent_splitter.addWidget(self.lista_preguntas)

        # Llenar la lista con los títulos
        for i in range(len(self.preguntas)):
            self.lista_preguntas.addItem(f"Pregunta {i+1}")

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
        self.label_referencia = QLabel("Referencia")
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
        label_pregunta = QLabel(f"{pregunta_data['pregunta']}")
        label_pregunta.setWordWrap(True)
        self.layout_pregunta_opciones.addWidget(label_pregunta)

        # 2. Opciones
        # Creamos un GroupBox o un QWidget simple para agrupar las opciones
        opciones_widget = QWidget()
        layout_opciones = QVBoxLayout(opciones_widget)
        layout_opciones.setContentsMargins(10, 10, 10, 10) # Pequeño margen
        
        for opcion in pregunta_data["opciones"]:
            radio_btn = QRadioButton(opcion)
            layout_opciones.addWidget(radio_btn)
        
        self.layout_pregunta_opciones.addWidget(opciones_widget)
        self.layout_pregunta_opciones.addStretch(1) # Relleno vertical
        
        # 3. Referencia
        self.label_referencia.setText(pregunta_data["reference"])

        # 4. Actualizar estado de los botones (desactivar si es el principio/fin)
        self.btn_anterior.setEnabled(self.indice_actual > 0)
        self.btn_siguiente.setEnabled(self.indice_actual < len(self.preguntas) - 1)

    # --- Métodos de Navegación ---
    @QtCore.Slot()
    def _navegar_por_lista(self, fila):
        """Maneja la navegación al hacer clic en un elemento de la lista."""
        self._cargar_pregunta(fila)
    
    @QtCore.Slot()
    def _anterior_pregunta(self):
        """Va a la pregunta anterior si existe."""
        if self.indice_actual > 0:
            self._cargar_pregunta(self.indice_actual - 1)
    
    @QtCore.Slot()
    def _siguiente_pregunta(self):
        """Va a la siguiente pregunta si existe."""
        if self.indice_actual < len(self.preguntas) - 1:
            self._cargar_pregunta(self.indice_actual + 1)
    
    @QtCore.Slot()      
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