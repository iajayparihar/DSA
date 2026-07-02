class RevNo:
    # tail recursion
    def rev(self,n):
        if n==0:
            return 
        print(n,end=' ')
        self.rev(n-1)
RevNo().rev(5) 

print()
class ForNo:
    # head recursion    
    def forv(self,n):
        if n==0:
            return 
        self.forv(n-1)
        print(n,end=' ')
ForNo().forv(5) 