import flet as ft

class QuestionList(ft.ListView):
    def __init__(self, questions):
        super().__init__()
        self._rows = len(questions)
        [self.controls.append(ft.Text(f'Pregunta {row+1}')) for row in range(self._rows)]
