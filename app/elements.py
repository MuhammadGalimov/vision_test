from django.template.loader import render_to_string


class Element:
    def __init__(self, T, value):
        if T not in {'title', 'text', 'button', 'subtitle'}:
            raise AttributeError

        self.T = T
        self.file = 'app/elements/' + self.T + '_element.html'
        self.value = value
        
    def render(self):
        return render_to_string(self.file, {self.T: self.value})
