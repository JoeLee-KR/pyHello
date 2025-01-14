#
#
#
import time

def isprime2(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def countprime(x):
    count = 0
    for i in range(2,x+1):
        #print(i, end='\r')
        if isprime2(i):
            count += 1
            print('\r' + '..count: ' + str(count) +'/' + str(i) + '...', end='')
        time.sleep(0.0001)
    print("[Done]\nFind:{}, in 1..{}.".format(count,x) )
    return count

print("Searched Number of Prime: ")
print("Total Prime Count is ", countprime(10000))
