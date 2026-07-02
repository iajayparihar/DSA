class fibbonaci:
    def fib(self, n):
        if n == 0 or n == 1:
            return n
        ans = self.fib(n-1) + self.fib(n-2)
        return ans

print(fibbonaci().fib(8))

def fibbo(n):
    if n == 0 or n == 1:
        return n
    f1 = 1
    f2 = 0
    f = 1
    for i in range(n+1):
        print(f)
        f2 = f1
        f1 = f
        f = f1 + f2

fibbo(5)
