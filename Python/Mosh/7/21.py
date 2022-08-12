# Add new method to str
class Text(str):
    def duplicate(str):
        return str+str

# modify list


class TrackableList(list):
    def append(self, object):
        print("APPENDED TO LIST")
        return super().append(object)


txt = Text("Dipu")
print(txt.duplicate())

t = TrackableList()
t.append(1)
