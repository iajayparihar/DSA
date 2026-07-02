#User function Template for python3

class Solution:
    def SumofDigits(self, A, B):
        expo = A**B
        s=0
        while expo > 0:
            s+=expo%10
            expo //= 10
        # print(s)

        def f(expo):
            s=0
            while expo > 0:
                s+=expo%10
                expo //= 10
            print(s)

        if len(str(s))==1:
            return s
        else: 
            f(s)    

k=Solution()
print(k.SumofDigits(21,5))

