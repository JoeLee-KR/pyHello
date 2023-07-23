# Section02-1
# basic codes
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print('Hello')
print("Hello")
print()

print("""HELLO py""")
print('''HELLO py''')
print()

print('T', 'e', 's', 't', sep='') # sep char is none
print('2019', '03', '29', sep='-') # sep char is -
print()

print('Welcome to', end=' ')
print('underslow ', end='')
print('World')
print('War')
print()

print('{} and {}'.format('JOE','LEE'))
print("{0} or {1} and {0}".format("LOVE", "ME"))
print("{a} and {b}".format(a='FUCK', b="YOU"))
print("%s and %d and %f" % (7.1,7.2,7.3))    # %s, %d, %f
print()

print("12345+++++12345+++++12345+++++12345+++++")
print("TEST: %5d, PRICE: %6.2f" % (77.123, 77.123))
#print("TEST: {0: 5d}, PRICE: {1: 6.2f}".format(  77.123,   77.123))
#this line cant work, and brock out at this point on run time.
print("TEST: {0: 5d}, PRICE: {1: 6.2f}".format(  88,   77.123))
print("TEST: {a: 5d}, PRICE: {b: 6.2f}".format(a=99, b=77.123))
print()

print("")
print()

# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""
# 기본 출력
print('Hello Python!')  # 문법적 중요
print("Hello Python!")  # 텍스트 의미
print("""Hello Python!""")
print('''Hello Python!''')

print()

# separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# file 옵션 사용
import sys

print('GeeksForGeeks', file=sys.stdout)

print()

print("%s's favorite number is %d" % ('Eunki', int(45)))

# format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{var1} are {var2}'.format(var1='You', var2='Niceman'))

# %d, %f, %s
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0:5d}, Price:{1:4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))