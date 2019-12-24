# Section05-2
#
#
v1 = 1
while v1 < 5:
    print("v1:", v1 , end=', ')
    v1 += 1
print()

#
for v2 in range(10):
    print("v2=%1d" % v2, end=', ')
print()

for v3 in range(1, 11):
    print("v3=%d" % v3, end=', ')
print()

for v4 in range(1, 11, 2):
    print("v4=%d" % v4, end=', ')
print()
print()

#
t = 1
tt = 0
while t < 11 :
    tt += t
    t +=1
print (t, tt)

ttt = range(1,10,1)
ttt4 = list( range(1,10,1) )
print(ttt, ttt4)
print( list( range(1,10,1) ) )
print()

#
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for aname in names:
    print("/", aname, end=' ')
print()
print(names)
print()

#
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

print("===", my_info)
print("===", dict( my_info.items()) )

for key in my_info:
    print(key, ":", my_info[key], end=' / ')
print()

for key in dict(my_info.items()):
    print(key, ":", my_info[key], end=' // ')
print()

for k, v in my_info.items():
    print(k, ":", v, end=' /// ')
print()

for val in my_info.values():
    print(val)
print()

#
# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:

    if num == 33:
        print("found33 : OK!")
        break
else:
        print("is not 33: ", num)


# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        print('FLOAT')
        continue
    print("type:", type(v), ".multiply by 3:", v * 3)

# 자료 구조 변환 예제
name = 'Niceman'
t = list(reversed(name) )
print('reversed : ', t )
print('list : ', list(t))
print('list : ', list(reversed(name)) )

t = tuple(reversed(name))
print('tuple : ', tuple(t) )
print('tuple : ', tuple(reversed(name)) )

t = set(reversed(name))
print('set : ', set(t))
print('set : ', set(reversed(name)))  # 순서X
