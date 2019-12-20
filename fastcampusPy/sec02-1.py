# Section02-1
# basic codes

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
