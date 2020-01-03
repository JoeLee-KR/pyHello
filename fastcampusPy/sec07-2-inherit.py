# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속 (java는 단일 상속과 인터페이스 방식으로 지원)

# 예제1
# 상속 기본
# 슈퍼클래스 및 서브클래스 -> 모든 속성, 메소드 사용 가능


class Car:
    """Parent Class"""
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        # print('Car Class "Show" Method! -in Print:' + self.type + "-" + self.color)
        return ('Car Class "Show" Method! -in return - at SUPER:' + self.type + "-" + self.color)


class PassCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # must? call superclass init
        self.car_name = car_name

    def show_model(self) : # None???
        #return ( 'Your PassCar Name : %s %s %s' % (self.car_name, self.type, self.color) )
        return ( 'Your Passcar Name : %s %s %s' % (self.car_name, self.type, self.car_name))


class Truck(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self):
        super().show()
        return 'Truck Info - : %s %s %s' % (self.car_name, self.color,self.type)

    def show_model(self) -> None:
        return 'Your Truck Name : %s' % self.car_name


# 일반 사용
model1 = PassCar('520d', 'sedan', 'red')

print("====================")
print("--Color:", model1.color)  # Super
print("--Type:", model1.type)  # Super
print("--Car Name:", model1.car_name)  # Sub
print("--Super show:", model1.show())  # Super
print("--Sub show_model:", model1.show_model())  # Sub
print("====================")

# Method Overriding
model2 = PassCar("220d", 'suv', 'black')
print("SS", model2.show())
print("SM", model2.show_model())
print("====================")

# Parent Method Call
model3 = Truck("350s", 'sedan', 'silver')
print("SS", model3.show())
print("SM", model3.show_model())
print("====================")

# Inheritance Info
print('Inheritance Info : ', PassCar.mro())
print('Inheritance Info : ', Truck.mro())


# 예제2
# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
print(A.mro())