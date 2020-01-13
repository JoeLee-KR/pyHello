# Section07-1   JOELEE
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 예제1

class UserInfo:
    def __init__(self, name):
        self.name = name
        # print("INIT:", name)

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")

print("===================== start ex 1")
user1 = UserInfo("Kim")
user2 = UserInfo("Park")
user3 = UserInfo("LLLL")

print(id(user1), "Object instance id")
print(id(user2), "Object instance id")
print(id(user3), "Object instance id")


user1.print_info()
user2.print_info()
user3.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)
print('user3 : ', user3.__doc__)

print(user1.name)
print(user2.name)
print("===================== end ex 1")
# 예제2
# self의 이해

class SelfTest:
    def function1():  # this is class method
        print("IN function1 called! im class method", id(SelfTest))

    def function2(self): # this is instance method
        print("IN function2: im instance method ", id(self))

f = SelfTest()
print("test2 =----------------")
print(dir(f))
print(dir(SelfTest))
print(f.__dict__)
print("test2 =----------------  SelfTest CLASS")
# f.function1()   is not called
SelfTest.function1()
print("===")
print("OUT id for class SelfTest: ",id(SelfTest))
print("===")
print("call calss method AAA: ", id(SelfTest.function1()) )
# print(SelfTest.function2()) #예외 발생
print("test2 =---------------- SelfTest F instance")
f.function2()
#print( f.function1(f), f.function1() )  #예외발생
print("===")
print("OUT id for instance f: ",id(f))
print("===")
print("call calss method BBB: ", id(f.function2()) )
print("===")
print("call calss method BBB: ", id(SelfTest.function2(f)) )
# python has self, therefore
# instance.method() == class.method(instance)
print("test2 =----------------")




# 예제3
# 클래스 변수 , 인스턴스 변수

class Warehouse:
    stock_num = 0  # class variable

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1
        print("__del__with value:", self.stock_num)


print("EX 3 ----------------------")
user1 = Warehouse('Kim')
user2 = Warehouse('Park')
print("create instance ...")

print(user1.name)
print(user2.name)
print("DICT instance user1: ", user1.__dict__)
print("DICT instance user1: ", user2.__dict__)
print("DICT class Warehouse: ", Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)
print("checkes ....")
# Warehouse.stock_num = 50 # 직접 접근 가능

print(user1.stock_num)
print(user2.stock_num)
print(Warehouse.stock_num)
print("checkes values ....")

Warehouse.stock_num += 10
print(user1.stock_num)
print(user2.stock_num)
print(Warehouse.stock_num)
print("checkes values ....")

del user1
del user2

print(Warehouse.stock_num)
print("checkes values after del ....")