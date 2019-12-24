# Sec04-4
#
# Dictionary & Set : data type is (Key:Value)
#
# Dict: 순서 x, 중복 x, 수정 o, 삭제 o   {k:v}
# Set : 순서 x, 중복 x, 수정 o, 삭제 o   set(list)
#

a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124', 'acct': 120 }
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4,5,6]}
ccc = {'Code001': a, 'Code002': c}

print(a)
print(ccc)
print(a['name'])  # dont use
print(a.get('name1'))
print(c['arr'][2:4])
print()

print('---------------')
a['address'] = 'Seoul'
a['rank'] = [1, 2, 3]
print('a - ', a)
print(a.keys())
tmp  = list(a.keys())
tmp2 = tuple(a.keys())
print(tmp)
print(tmp2)
print(tmp[1:3])
print(tmp2[1:3])
print(a.values())
print(a.items())
print(list(a.items()))
print('name' in a)
print('kim' in a)  # only key
print('Kim' in a)  # only key

print('=================')
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])

tt = tuple(b)
ll = list(b)
print(tt)
print(ll)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)
print(s1.union(s2))
print(s1 | s2)
print(s1.difference(s2))
print(s1 - s2)
print(s2 - s1)

print('==========')
s1.add(11)
s2.add(12)
print(s1 | s2)
s2.remove(12)
# s2.remove(11)
print(s1 | s2)
