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
        print("INIT with NONE")
        self.name = "NEWNONE"

    def __init__(self, name):
        self.name = name
        print("INIT:", name)

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
print(UserInfo.name, user1.name)

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
# ref: sec07-1a-class.py


# 예제3
# 클래스 변수 , 인스턴스 변수
# ref: sec07-1b-class.py