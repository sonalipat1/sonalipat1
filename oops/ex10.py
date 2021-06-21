class Car:
    def turn_on(self):
        print("you start the engin")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brakes(self):
        print("you step on brakes")
        return self
    def  turn_off(self):
        print("you turn offfg the engine")
        return self

car= Car()
car.turn_on().drive()
car.brakes().turn_off()