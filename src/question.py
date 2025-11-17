import flet as ft

class Question(ft.Column):
    def __init__(self,question):
        super().__init__()
        self._question = question['pregunta']
        self._options = question['opciones']
        self._answer = question['respuesta']
        self._referencia = question['referencia']

        #set widgets
        self.text_view = ft.Text(self._question)
        self._answer_options = ft.RadioGroup(content=ft.Column([ft.Radio(value=option, label=option) for option in self._options]))
        self._reference = ft.Text(f'Referencia: {self._referencia}')

        self.controls = [self.text_view, self._answer_options, self._reference]
