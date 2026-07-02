class recursion:
# fibbonachi
    def recq(self,n):
        if n<=1:
            return n
        else:
            return (self.recq(n-1)+self.recq(n-2))

k=recursion()
num=int(input("Enter the NUMBER :- "))
for i in range(num):
    a=k.recq(i)
    print(a)


# def recq(n,f1,f2,f):
#     if n!=0:
#         f=f1+f2
#         f1=f2
#         f2=f
#         print(f)
#         recq(n-1,f1,f2,f)

# num=int(input("Enter the NUMBER :- "))
# f1=-1 ; f2=1 ; f=0
# recq(num,f1,f2,f)