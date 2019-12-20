# Section02-2
#
#

# import this
import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)

print("My name is Doogie")
myName = "Doogie Dog"
print('My Name is ',myName, sep='')

if myName == 'Doogie Dog':
    print('OK')

for i in range(1,4):
    for j in range(1,3):
        print('%d+%d=' %(i,j), i*j,sep='')

def fPrintG():
    print('HELLO....')

fPrintG()


class Cookie:
    pass

cookie = Cookie()

print(id(cookie))
print(dir(cookie))

print(id(Cookie))
print(dir(Cookie))


