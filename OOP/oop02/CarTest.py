class Car:
    def __init__(self):
        self.speed=0
    def drive(self):
        self.speed=60

if __name__ == '__main__':
    myCar = Car()
    myCar.speed = 0
    myCar.color = 'Blue'
    myCar.model = 'E-Class'

    print('자동차 객체를 생성하였습니다.')
    print('자동차의 속도는', myCar.speed)
    print('자동차의 모델은', myCar.model)
    print('자동차의 색깔은', myCar.color)
    myCar.drive()
    print('자동차의 속도는', myCar.speed)