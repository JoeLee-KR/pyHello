# Section05-1
#

if True:
    print("Yes True")  # 들여쓰기 중요
else:
    print("No False")

# 참 거짓 종류
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0, None
if None :
    print("2Yes True")  # 들여쓰기 중요
else:
    print("2No False")

#
#
#
id1 = "gold"
id2 = "admin"
grade = 'super'

if id1 == "agold" or id2 == "aadmin":
    print("관리자 로그인 성공")

    if id2 == "admin" and grade == "super":
        print("최고 관리자 로그인 성공")

#
num = 70
if num >= 70:
    print("num over 70 ", num)
elif num >= 60:
    print("num 60~69 ", num)
else:
    print("default numis under 59")

#
q = [1, 2, 3]
w = {7, 8, 9, 9}
e = {"name": 'Kim', "city": "seoul", "grade": "B"}
r = (10, 12, 14)

print(1 in q)
print(6 in w)
print(12 not in r)
print("name" in e)  # key 검색
print("seoul" in e.values())  # value 검색
