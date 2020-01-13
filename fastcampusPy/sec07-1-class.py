# Section07-1   JOELEE
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 예제1

class UserInfo:
    name = "NONE"
    def __init__():
        #print("INIT with NONE")
        self.name = "NEWNONE"

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
user3 = UserInfo("JOE")

print(id(user1), "Object instance id")
print(id(user2), "Object instance id")
print(id(user3), "Object instance id")
print(UserInfo.name)

user1.print_info()
user2.print_info()
user3.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)
print('user3 : ', user3.__doc__)

print(user1.name)
print(user2.name)
print(user3.name)
print("===================== end ex 1")

# 예제2
# self의 이해

class SelfTest:
    def function1():  # this is class method
        print("IN function1 called! im class method", id(SelfTest))
        # MUST called by ClassName

    def function2(self): # this is instance method
        print("IN function2: im instance method, this is instance id: ", id(self))
        # MUST called by InstanceName after Create


print("1111 -------------------------------- SelfTest Class")
print(dir(SelfTest))

f = SelfTest()
f2 = SelfTest()
print(dir(f))
#print(SelfTest.__dict__) $ cant call, SelftTest is class
print(f.__dict__)
SelfTest.function1()
#f.function1()          # cant call, function1() is class method

print(".............")
print("OUT id for class SelfTest(): ", id(SelfTest))
print("OUT id for class SelfTest.f(): ", id(SelfTest.function1()) )

print("22222 =============================== F Instance")
# print(SelfTest.function2()) #예외 발생
# SelfTest.function2() # 예외 발생
SelfTest.function2(f)
f.function2()
print("*** SAME CALL & USE: Selftest.f2(f) == f.f2()")
#print( f.function1() )  #예외발생
#print( f.function1(f) )  #예외발생
print(".............")
print("OUT id for instance f: ",id(f))
print("call calss, id for method : ", id(f.function2()) )
print("call calss, id for method : ", id(SelfTest.function2(f)) )
# python has self, therefore
# instance.method() == class.method(instance)

print(".............")
print("OUT id for instance f: ",id(f2))
print("call calss, id for method : ", id(f2.function2()) )
print("call calss, id for method : ", id(SelfTest.function2(f2)) )
print("END SelfTest =------------------------")




# 예제3
# 클래스 변수 , 인스턴스 변수

class Warehouse:
    stock_num = 0  # class variable

    def firstWarehouse():
        this.stock_num += 10

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1
        print("__del__with value:", self.stock_num)


print("EX 3333333 ----------------------")
user1 = Warehouse('Kim')
user2 = Warehouse('Park')
user3 = Warehouse("JOELEE")
print("create instance ...")

print(user1.name)
print(user2.name)
print(user3.name)
print("DICT instance user1: ", user1.__dict__)
print("DICT instance user1: ", user3.__dict__)
print("DICT class Warehouse: ", Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)
print(Warehouse.stock_num)

Warehouse.stock_num += 20
print("Warehouse1: ", Warehouse.stock_num)
# Warehouse.stock_num = 50 # 직접 접근 가능

Warehouse.stock_num += 20
#Warehouse.firstWarehouse()
print("Warehouse2: ", Warehouse.stock_num)  # 클래스 네임스페이스 , 클래스 변수 (공유)
print("checkes ....")

print(user1.stock_num)
print(user2.stock_num)
print(Warehouse.stock_num)
print("checkes values ....")

del user1
del user2
del user3

print(Warehouse.stock_num)
print("checkes values after del ....")