class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    
    def __str__(self):
        msg = str(self.color)
        return msg

if __name__ == '__main__':
    myCar = Car(0, 'blue', 'E-class')
    dadCar = Car(200, '화이트', '아반떼')
    print(myCar)
    print(dadCar)