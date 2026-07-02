def insort(A):
    length=len(A)
    for i in range(1,length):
        temp=A[i]
        j=i-1
        # base codition j>=0
        while j>=0 and A[j]>temp :
            A[j+1]=A[j]
            j-=1
        
        A[j+1]=temp

arr=[5,4,10,1,6,2]
print(arr)
insort(arr)
print(arr)