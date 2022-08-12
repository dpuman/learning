from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TEXT")


class DropDownList(UIControl):
    def draw(self):
        print("Drop")


def draw(control):
    return control.draw()


tb = TextBox()
draw(tb)
ddl = DropDownList()
draw(ddl)
