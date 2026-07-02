class factorial:
    def fact(self, n):
        if n == 0:
            return 1
        return n * self.fact(n-1)

k=factorial()
a=k.fact(6)
print(a)
