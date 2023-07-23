# 예제3
# 클래스 변수 , 인스턴스 변수

class Warehouse:
    stock_num = 0  # class variable

    def firstWarehouse(self):
        self.stock_num += 11

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1
        print("__del__with value:", self.stock_num)


print("sec07-1b-class ---------------------- 1111")
user1 = Warehouse('Kim')
user2 = Warehouse('Park')
user3 = Warehouse("JOELEE")
print("create instance ...")

print(user1.name, end=' ')
print(user2.name, end=' ')
print(user3.name)
print("DICT instance user1: ", user1.__dict__)
print("DICT instance user2: ", user2.__dict__)
print("DICT instance user3: ", user3.__dict__)
print("DICT class Warehouse: ", Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)
print("class's variable sotck_num:", Warehouse.stock_num)

Warehouse.stock_num += 20
print("class's variable sotck_num:", Warehouse.stock_num)
Warehouse.stock_num = 50
print("class's variable sotck_num:", Warehouse.stock_num)
# Warehouse.stock_num = 50 # 직접 접근 가능

print("checkes ....start")
print("user1/2/3.stock_num, Warehouse.stock_num: ", user1.stock_num, user2.stock_num, user3.stock_num, Warehouse.stock_num)

print("checkes ....1")
user1.firstWarehouse()
print("user1/2/3.stock_num,  Warehouse.stock_num: ", user1.stock_num, user2.stock_num, user3.stock_num, Warehouse.stock_num)

print("checkes ....2")
user2.firstWarehouse()
print("user1/2/3.stock_num, Warehouse.stock_num: ", user1.stock_num, user2.stock_num, user3.stock_num, Warehouse.stock_num)

print("checkes ....W")
#Warehouse.firstWarehouse()     # is not work
Warehouse.firstWarehouse(user1)
print("user1/2/3.stock_num, Warehouse.stock_num: ", user1.stock_num, user2.stock_num, user3.stock_num, Warehouse.stock_num)

print("checkes ....3")
user3.firstWarehouse()
user3.firstWarehouse()
user3.firstWarehouse()
print("user1/2/3.stock_num, Warehouse.stock_num: ", user1.stock_num, user2.stock_num, user3.stock_num, Warehouse.stock_num)

del user1
print(Warehouse.stock_num)
del user2
print(Warehouse.stock_num)
del user3
print(Warehouse.stock_num)

print("checkes values after del ....")