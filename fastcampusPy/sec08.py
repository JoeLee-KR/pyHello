# Section08
# 파이썬 모듈과 패키지

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)
from fastcampusPkg.fibonacci import Fibonacci

print("ex1-1 : ", Fibonacci.fib(100))
print("ex1-2 : ", Fibonacci.fib2(200))
print("ex1-3 : ", Fibonacci().title)

fff = Fibonacci("JOE")
print("ex1-4 : ", fff.fib3(100), fff.title)
#print("ex1-5 : ", fff.fib(100), fff.fib2(100))
# dont call with instance name to CLASS METHOD...

# 사용2(클래스)
from fastcampusPkg.fibonacci import *

print("ex2 : ", Fibonacci.fib(300))
print("ex2 : ", Fibonacci.fib2(400))


# 사용3(클래스)
from fastcampusPkg.fibonacci import Fibonacci as fb

print("ex3 : ", fb.fib(130))
print("ex3 : ", fb.fib2(400))


# 사용4(함수) : 파일 Alias as c
import fastcampusPkg.calc as c

print("ex4 : ", c.add(10,10), c.mul(10,4))


# 사용5(함수) : 파일.{imported}.Function Alias as d
from fastcampusPkg.calc import div as d

print("ex5 : ",     d(100,10), int(d(100,10)))

# 사용6
import fastcampusPkg.prints as p
import builtins
# builtins is default included Package, that has normally function

p.prt1()
p.prt2()
print(dir(p))
print(dir(builtins))
