# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속 (java는 단일 상속과 인터페이스 방식으로 지원)

# 예제1
# 상속 기본
# 슈퍼클래스 및 서브클래스 -> 모든 속성, 메소드 사용 가능


class Car:
    """Parent Class : Super Class"""
    def __init__(self):
        self.type = "NA_type"
        self.color = "NA_color"

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        # print('Car Class, "Show" Instance Method! - at SUPER: ' + self.type + "-" + self.color)
        return ('Car::Show Instance Method! - at SUPER: ' + self.type + " " + self.color)


class Sedan(Car):   # 'Cas' is a parent class
    """Child Class : Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
            # ............................
            # must? call superclass init
            # multiple superclass?
            # ............................
        self.car_name = car_name

    def show_model(self) -> None:
        #return ( 'Your Sedan Name : %s %s %s' % (self.car_name, self.type, self.color) )
        return ( 'Your Sedan : %s %s %s' % (self.car_name, self.type, self.color))


class Truck(Car):   # 'Cas' is a parent class
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self):
        super().show()
        return 'Truck Info Show @instance- : %s %s %s' % (self.car_name, self.color,self.type)

    def show_model(self) -> None:
        return 'Your Truck Name1 : %s' % self.car_name

    def show_model2(self) :
        return 'Your Truck Name2 : %s' % super().show()


print("==================== 111111")
# 일반 사용
model1 = Sedan('520d', '4family', 'red')

print("--Color:", model1.color)  # Super
print("--Type:", model1.type)  # Super
print("--Car Name:", model1.car_name)  # Sub
print("--Super show:", model1.show())  # Super
print("--Sub show_model:", model1.show_model())  # Sub


print("==================== 222222")
# Method Overriding
model2 = Sedan("740i", 'DeluxFamily', 'black')

print("--Super show:", model2.show())
print("--Sub show_model:", model2.show_model())

print("==================== 33333333")
# Parent Method Call
model3 = Truck("F960", 'CarGo', 'silver')
print("SS", model3.show())
print("SM", model3.show_model())
print("SM", model3.show_model2())
print("====================")

# Inheritance Info
print('Inheritance Info for CLASS : ', Sedan.mro())
print('Inheritance Info for CLASS : ', Truck.mro())


# 예제2
# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class AAA(X, Y):
    pass


class BBB(Y, Z):
    pass


class LastM(BBB, AAA, Z):
    pass

print("AAAAAAAA")
print(AAA.mro())

print('LLLLLLLLLLL')
print(LastM.mro())