class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def eat(self):
        print(self.name,'가 음식을 먹습니다.')
    def play(self):
        print(self.name,'가 놀고 있습니다.')
    def run(self):
        print(self.name,'가 뛰어다닙니다.')
    
class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def eat(self):
        print(self.name,'가 음식을 먹습니다.')
    def play(self):
        print(self.name,'가 놀고 있습니다.')
    def run(self):
        print(self.name,'가 뛰어다닙니다.')

if __name__ == '__main__':
    mary = Cat('메리', 3, '갈색')
    tomy = Dog('토미', 2, '흰색')
    print(mary.name,'가(고양이) 탄생하였습니다.')
    tomy.run()
    mary.eat()
  