class Expo:
    def power(self,a,b):
        # base case
        if b == 0 :
            return 1
        if b == 1 :
            return a

        ans = self.power(a, b//2)

        if b%2 == 0 :
            return ans * ans
        else:
            return a * ans * ans

ans=Expo().power(3, 10)
print(ans)