class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title

    def fib(n) -> None:
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()

    def fib2(n):
        result = []
        print ("====", n)
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        return result

    def fib3(nnn) -> None:
        a, b = 0, 1
        print(a,b,nnn)

if __name__ == "__main__":
    print("This is", dir())
    ff2 = Fibonacci("JOE FIB")
    print(ff2.title)
    ff = Fibonacci()
    print(ff.title)
    #ff.fib()
    #print(ff.fib2(5))
    ff.fib3()
    Fibonacci.fib(5)
    Fibonacci.fib2(5)

