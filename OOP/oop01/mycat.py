class Cat:
    def __init__(self):
        self.name = "야옹이~"
        self.color = "화이트"
    def showName(self):
        print(self.name)
    def showColor(self):
        print(self.color)

if __name__ == "__main__":
    cat = Cat()
    cat.showName()
    cat.showColor()