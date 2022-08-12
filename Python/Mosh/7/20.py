class TextBox():
    def draw(self):
        print("TEXT")


class DropDownList():
    def draw(self):
        print("Drop")


def draw(control):
    return control.draw()


tb = TextBox()
draw(tb)
ddl = DropDownList()
draw(ddl)
