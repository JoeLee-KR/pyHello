# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 함수 호출
# function_name()
# **** 함수 선언 위치 중요


# 예제1
def hello(world):
    print("Hello, ", world, sep='')

param1 = "Niceman"
hello(param1)


# 예제2
def hello_return(world):
    value = "Hello, " + str(world)
    return value

str = hello_return("Niceman****")
print(str)


# 예제3(다중리턴)

def func_mul1(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3

val1, val2, val3 = func_mul1(3)
print(type(val1), val2, val3)


# 튜플 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return (y1, y2, y3)

tup = func_mul2(4)
print('A', type(tup), tup, list(tup))


# 리스트 리턴
def func_mul2(x):
    y1 = x * 3
    y2 = x * 5
    y3 = x * 7
    return [y1, y2, y3]  # return type list

tup = func_mul2(4)
print('B', type(tup), tup, list(tup), set(tup))


# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'ret1': y1, 'ret2': y2, 'ret3': y3}


dic = func_mul3(8)

print('C', type(dic), dic, dic.get('ret3') )
print('C', dic.items() )
print('C', dic.keys() )
print('C', dic.values() , "===")


# 예제4
# *args, **kwargs 이해
print("----------args.........")
# *args
def args_func(*args):  # 매개변수명 자유롭게 변경 가능 // TUPLE로 인수를 처리함
    for i, v in enumerate(args):
        print('{}'.format(i), ":", i, "::", v, end=' , ')
    print('<<')

#def args_func(*args):
#    for v in args:
#        print(v, end='')
#    print('>>')

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print()

print("----------kwargs.........")
# kwargs
def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능 // DICT로 인수를 처리함
    for k in kwargs.keys():
#        print('{}'.format(k), kwargs[k], '##', k, end=' ')
        print( '>>>',  k, kwargs[k], end=' ')
    print('FFF')

#def kwargs_func(**kwargs):
#    for v in kwargs.keys():
#        print(kwargs.items(), end=' ')
#    print('FF')

#def kwargs_func(**kwargs):
#    for k, v in kwargs.items():
#        print (k,v)
#    for k in kwargs.keys():
#        print(k, kwargs[k])
#    for v in kwargs.values():
#        print(v)

kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

dd = { 'name1':'joe', 'name2': 'lee' }
print( dd.items() )
kwargs_func( **dd)
print()


print("========= complexed args ........")
# 전체 혼합
def example_a(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)


example_a(10, 20, 30, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)
example_a(10, 20, 30, age1=33, age2=34, age3=44)
example_a(10, 20,  age1=33, age2=34, age3=44)
example_a(10, 20 )

print("========= nested function ........")
# 예제5
# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In func")
    func_in_func(num + 100)

nested_func(1)

# 실행불가
# func_in_func(1)

print("========= HINT for return values ........")
# 예제6
# Hint
def tot_length1(word: str, num: int) -> int:
    return len(word) * num

print('hint exam1 : ', tot_length1("ilove you", 10))


def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

tot_length2("niceman", 10)


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화

# 예제7
# def mul_10(num):
#     return num * 10

# def mul_10_one(num): return num * 10
#
# lambda x: x * 10

# 일반적 함수 -> 변수 할당 //객체로 할당됨을 알 수 있음
def mul_10(num):
    return num * 9


mul_func = mul_10

print(mul_func(5))
print(mul_func(6))

print("-----------lambda")
# 람다 함수 -> 할당
lambda_mul_x = lambda nnn: nnn * 8
print('>>>', lambda_mul_x(3))


print("-----------arg with function reference")
def func_final(x, y, funcarg):
    print(x * y * funcarg(4))


func_final(10, 10, lambda_mul_x)
func_final(10, 10, mul_func)