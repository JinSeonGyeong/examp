class person:
    def __init__(self):
        self.hello = "안녕하세요."
        self.color = "빨간색"
    def greeting(self):
        print(self.hello)
    def showColor(self):
        print(self.color)
james = person() # 객체생성법
james.greeting()
james.showColor()