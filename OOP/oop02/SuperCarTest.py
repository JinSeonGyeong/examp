class Car:
    def run(self):
        print('달리다')

class SuperCar(Car):
    def run(self):
        print('수퍼카 달리다')
    def FastRun(self):
        print('빠르게 달리다')

if __name__ == '__main__':
    tico = SuperCar()
    tico.FastRun()
    tico.run()