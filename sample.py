class Square:
    def __init__(self):
        self.length = int(input("length : "))
        self.width = int(input("Width : "))
        self.area = self.length * self.width


class Box(Square):
    def __init__(self):
        super().__init__()
        self.height = int(input("Height : "))
        self.volume = Square().length * Square().width * self.height


b1 = Box()
print(b1.area)
print(b1.volume)