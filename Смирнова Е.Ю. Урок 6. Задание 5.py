class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Для того, чтобы использовать {self.title} необходимо заменить стержень."


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Для того, чтобы использовать {self.title} необходимо его заточить."

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Для того, чтобы использовать {self.title} необходимо его заправить."

p = Pen("ручку")
k = Pencil("карандаш")
m = Handle("маркер")
print(p.draw())
print(k.draw())
print(m.draw())