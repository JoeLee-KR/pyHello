#
# This is CLASS defininition, for using at CLASS status
#
class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title

    def fib(n) -> None:
        a, b = 0, 1
        while a < n:
            print(a, end=':')
            a, b = b, a + b
        print( '== fib CLASS method with ', n)

    def fib2(n):
        result = []
        #print ("====", n)
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        print(result, '== result list, fib2 CLASS method with ', n)
        return result

    def fib3(self, n) -> None:
        a, b = 0, 1
        while a < n:
            print(a, end=':')
            a, b = b, a + b
        print( '== fib3 OBJECT method with', n)

#
# Individual Self Test Code
#
if __name__ == "__main__":
    print('========= FIBONACCI PKG self test ========')
    print("This is", dir())

    print("Class Finonacci::")
#    print("Fibonacci.title = ", Fibonacci.title  ) # not access to instance variable
    Fibonacci.fib(30)
    Fibonacci.fib(100)
    Fibonacci.fib2(100)

    print("Instance Fibonacci ff ::")
    ff = Fibonacci()
    print("ff.title = ", ff.title)
    ff.fib3(50)

    print("Instance Fibonacci ff2 ::")
    ff2 = Fibonacci("JOE FIB")
    print("ff2.title = ", ff2.title)
#    ff.fib3(50)        # not access class method
    ff.fib3(50)
    #ff.fib()           # not access class method
    #print(ff.fib2(5))  # not access class method

    print("Instance Fibonacci aFib ::")
    aFib = Fibonacci("3RD")
    print("aFib.title = ", aFib.title)
    aFib.fib3(50)

