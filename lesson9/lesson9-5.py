class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")

class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")

class Handle(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} handle!")

s = Stationery()
s.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Pentel")
pencil.draw()
handle = Handle("Brauberg")
handle.draw()