#
#
#
# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print('1:', len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('2:','apple;orange;banana;lemon')

# 3. 화면에 * 기호 100개를 표시하세요.
print('3:','*'*5, '*'*2)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
t="30"
print('4:', int(t), float(t), complex(t), t )

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
t = 'Niceman'
print('5:', t[4:7])
print('5:', t[t.index("man"):])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
t='Strawberry'
tt=list(reversed(t))
print('6:', tt )
print('6:', tt[0] )
print('6:', t[::-1] )
t = t[::-1]
print('6:', t )

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
t = "010-7777-9999"
import re
print('7:', re.sub('[^0-9]', '', t) )
print('7:', re.sub('[\-]', '', t) )

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
print('8:' )

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
print('9:', "Niceman".upper() )

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
print('10:', )

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
t = ["Banana", "Apple", "Orange"]
t.remove("Apple")
print('11:', t )

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
t = (1,2,3,4)
tt = list(t)
print('12:', tt, t)
t = [1,2,3,4]
tt = tuple(t)
print('12:', tt, t)

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
t = {'성인': 100000 , '청소년' : 70000 , '아동' : 30000 }
print('13:', t )

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
t['소아'] = 0
#t.add( {'소아':0})
print('14:', t)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print('15:', t.keys() )
print('15:', list(t.keys()) )
ttt = list(t.keys())
print('15:', ttt)

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print('16:', t.values() )
print('16:', list( t.items() ) )
# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
