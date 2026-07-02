
def select_largest_one(A,l):
    for i in range(l-1,-1,-1):
        # print(i)
        m=i 
        for j in range(i+1):
            # find greatest element in the array
            if A[m]<A[j]:
                m=j
        if A[i]<A[m]:
            #swap
            A[m],A[i]=A[i],A[m]
            
            
arr=[1,7,4,10,8,3,1]
length=len(arr)
select_largest_one(arr, length)
print(arr)