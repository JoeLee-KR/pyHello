# Section04-1
#
# data type
'''
 tuple
 lists []
 sets  {}
 dictionaries {:}
'''

vstr = "Nicname";
vstr2 = 'Nicname';
vbool = True

vtuple = 3,5,7,9
vlist = [3,4,5,6,7]
vset = {13,15,17}
vdict = {
    "name" : "Kim",
    'age' : 24
}

print(type(vdict))
print(type(vtuple))
print(type(vset))
print(type(vlist))
print(type(vbool))

smallint1 = 12
bigint1 = 12345678901234567890
f1 = 1.0
f2 = .888

print('===')
print( smallint1 + f1)
rrr = bigint1 * f1
print(bigint1)
print(rrr)
print(int(rrr))

print('===')
print(bigint1 * bigint1)
print(bigint1)
print(int('3123'))

print('===')
n, m = divmod(100,8)
print(n,m)

import math
print(math.ceil(5.1))  # 5.1보다 크고 가장 작은 정수
print(math.floor(3.87)) # 3.87보다 작고 가장 큰 정수