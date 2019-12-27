# Sec04-3
#
# data type
'''
 tuple
 lists []
 sets  {}
 dictionaries {:}
'''

# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)  [], list()
# dictinaries와 더불어 가장 많이 사용함
# 튜플 자료형(순서O, 중복O, 수정X,삭제X)  (), list()

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

c = [1,2,3]
d = ['a', 'bb', 'ccc']
cc = [1,2,'a','b']
dd = [1,2,[3,4,'aaa','bbbb', 'cccc']]

print('============')
print(cc, "X", dd)
print(dd[0], dd[1], dd[2], cc[2], dd[2][2], dd[-1][-1] )
print(dd[1:5])
print(dd[2:5])
print(dd[2][1:3])

print(cc + dd)
print(cc *2)
#print(cc * dd)

print('============')
print(cc)
cc[0]=77
print(cc)
cc[0:0] = [88, 99]
print(cc)
cc[0:3] = [1]
print(cc)

print('-----------')
print(cc)
cc[1:2] = [ 'jj', 'kk']  # insert
print(cc)
cc[1] = ['k','o','r']  # replace at 1
print(cc)
del cc[0]
print(cc)
del cc[-1]
print(cc)

print('============')
y =[ 5,2,3,1,4, 0]
print('a', y)
y.append(7)
print('b', y)
y.sort()
print('c', y)
y.reverse()
print('d', y)
y.insert(2,9)
print('e', y)
y.remove(2)
print('f', y)
x = y.pop()
print('g', y, x)
# y.push(8)
print('z', y)


#
#
#
# 선언
a = []
b = list( (33,44) )
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Cap', 'Plate']
e = [10, 100, ['Pen', 'Cap', 'Plate']]

# 인덱싱
print('#=====#++++++++++++++++++ INDEXING')
print(b)
b[1] = 55
print(b)
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][2][4])
print('e - ', list(e[-1][2]))

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[3:])
print('e - ', e[2][0:2])

# 리스트 연산
print('#=====# list calc')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 리스트 수정, 삭제
print('#=====#')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)
a.append(6)
print('aac - ', a.count(6))
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(5))
a.insert(2, 7)
print('a - ', a)
a.reverse()
print('aaa- ', a)
a.remove(6)
print('aa - ', a)
print('aa - ', a.pop())
print('aa - ', a.pop())
print('aa - ', a)
print('aac - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('aaa last - ', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    l = a.pop()
    print('poped:',l, 'then', l is 2)

# 튜플 자료형(순서O, 중복O, 수정X,삭제X)

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, 'Pen', 'Cap', 'Plate')
e = (10, 100, 1000, ('Pen', 'Cap', 'Plate'))

# 인덱싱
print('#=====#*************** TUPLE')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][2][4])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('#=====#---- SLICE')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', d[2:3])
print('e - ', e[3][1:3])
print('eee - ', e[2])
print('eee - ', e[2:3])
print('eee - ', e[2:4])

# 튜플 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 튜플 함수
a = (5, 4, 2, 3, 1, 4)

print("****************")
print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.index(4))
print('a - ', a.count(4))
# print('a - ', a.sort(4))