def selection(A):
    length=len(A)
    for i in range(length-1):
        m=i
        for j in range(1+i,length):
            # this condition find the smallest value 
            # and put that value into the m variable

            if A[m]>A[j]:
                m=j
        # if a[i] is graterthan , we find the samllest one , then swap
        if A[i]>A[m]: 
            A[i],A[m]=A[m],A[i]

arr=[1,7,4,10,8,3,1]
print("Array",arr)
selection(arr)
print("Sorted Array :- ",arr)