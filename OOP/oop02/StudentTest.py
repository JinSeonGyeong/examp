class Person:
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    def study(self):
        print('공부하기')

if __name__ == '__main__':
    x = Student()
    x.greeting()
    x.study()