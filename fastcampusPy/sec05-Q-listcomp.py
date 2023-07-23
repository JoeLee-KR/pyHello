# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

#
# List Comprehension
#
number = []
for n in range(1,11):
    number.append(n)
print(number)

number2 = [ x for x in range(1,11) ]
print(number2)

#
#
#

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print('1.', q1['가을'], q1.get('가을') , end=' ')
for i in q1.keys() :
    if i == '가을' :
        print(q1.get(i))

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과", "겨울":"사과"}
print('2. Find 사과:' , end=' ')
for k, v in q2.items() :
#    if ( k == '사과' or v == '사과') :
    if '사과' in (k,v) :
        print('Exist: ', k,v)
        break
else :
    print('Not exist Apple')


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
v = 101
if ( v >= 81 and v <= 100 ):
    print('3. ', v , 'is', 'A')
elif ( v >= 61 and v <= 80 ) :
    print('3. ', v , 'is', 'B')
elif ( v >= 41 and v <= 60 ) :
    print('3. ', v , 'is', 'C')
elif ( v > 100 or v < 0 ) :
    print('3. ', v , 'is not valid')
else :
    print('3. ', v , 'is', 'F')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
lv = [12,6,10, 13]
mlv = 0
for i in lv:
    if mlv < i :
        mlv = i
print('4. ', mlv)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
v = '7003291389923'
if v[6] == '1' or v[6] == '3' :
    print('5. ', v, 'is Man')
else:
    print('5. ', v, 'is Women')

vv = int(v[6])
if vv % 2 == 1 :
    print('5. ', v, 'is Man')
else:
    print('5. ', v, 'is Women')
# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
print('6. ', end='')
for v in q3:
    if v == '정':
        continue
    print(v, end = ' ')
print()

qq3 = []
qq3 = [ x for x in q3 if x !='정' ]
print ('66. ', qq3)


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
print('7. ', end=' ')
for n in range(1,101):
    if n % 2 != 0:
        print(n, end=' ')
print()

print('77.', end='')
nn = [ x for x in range(1,101) if x % 2 != 0]
print (nn)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
print('8. ', end=' ')
for v in q4:
    if len(v) >= 3 :
        print(v, end=' ')
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print('9. ', end=' ')
for vv in q5:
    if vv.islower():
        print(vv, end='')
print()

vvv = [ vv for vv in q5 if vv.islower()]
print("99. ", vvv, end='' )
for vx in vvv:
    print(vx, end='')
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
qq = ''
print('10. ', end=' ')
for v in q6 :
    qq += v
    if v.islower() :
        print(v.upper(),end='')
    else:
        print(v.lower(),end='')
print()
print('10. ', qq)

