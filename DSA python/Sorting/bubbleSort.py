def bubble(A):
    length=len(A)
    for i in range(length):
        for j in range(length-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j] #swap
    return # there is no matter of return 

arr=[5,2,1,4,0,7,12,0]
l=len(arr)
print(l)
bubble(arr)
print(arr)

'''----------------'''

def bbl(arr,l):
    for i in range(l):
        for j in range(l-1-i): # this loop is not executed for zero 
            pass    
        print(l-1-i)
        
        if arr[j]>arr[j+1]:
            #swap
            arr[j],arr[j+1] = arr[j+1],arr[j]
    # print(arr)

arr=[5,2,1,4,0,7,12,0]
bbl(arr,len(arr))
