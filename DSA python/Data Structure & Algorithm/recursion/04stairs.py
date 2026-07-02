class Stairs:
    def countStr(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 1

        # if n == 0 or n == 1:
        #     return n

        return self.countStr(n-1) + self.countStr(n-2)
        
print(Stairs().countStr(5))
