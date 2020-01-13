class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title

    def fib(n) -> None:
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print( '== fib')

    def fib3(self, n) -> None:
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print( '== fib')

    def fib2(n):
        result = []
        #print ("====", n)
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        print(result, '== fib2')
        return result

if __name__ == "__main__":
    print("This is", dir())
    ff2 = Fibonacci("JOE FIB")
    print(ff2.title)
    ff = Fibonacci()
    print(ff.title)
    #ff.fib()
    #print(ff.fib2(5))
    Fibonacci.fib(100)
    Fibonacci.fib2(100)

