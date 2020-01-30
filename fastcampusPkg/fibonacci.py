#
# This is CLASS defininition, for using at CLASS status
#
class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title

    def fib(n) -> None:
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
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
            print(a, end=' ')
            a, b = b, a + b
        print( '== fib3 OBJECT method with', n)

#
# Individual Self Test Code
#
if __name__ == "__main__":
    print('========= FIBONACCI PKG test ========')
    print("This is", dir())

    ff = Fibonacci()
    print("ff.title = ", ff.title)

    ff2 = Fibonacci("JOE FIB")
    print("ff2.title = ", ff2.title)

    #ff.fib()
    #print(ff.fib2(5))
    Fibonacci.fib(30)
    Fibonacci.fib(100)
    Fibonacci.fib2(100)

    aFib = Fibonacci("3RD")
    aFib.fib3(70)
