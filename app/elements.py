from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def generate_html(self):
        pass


class TitleElement(Element):
    pass


class TextElement(Element):
    pass


class BackgroundElement(Element):
    pass


class ButtonElement(Element):
    pass


class SubtitleElement(Element):
    pass


class FormElement(Element):
    pass
