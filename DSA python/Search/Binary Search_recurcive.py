# finding index of the element in array by recursive method

def BSrecursive(arr,key,l,r):
    #base condition 
    mid = (l+r)//2
    if key == arr[mid]:
        print("key id at indexd =",mid)
        return mid
    if l<=r:
        if key >= arr[mid+1]:
            BSrecursive(arr, key, l=mid+1,r=r)
        else:
            BSrecursive(arr, key, l,r=mid-1)
    return -1

A=[12,15,20,25,26,39,41,51,53,59,62,71,1]
A.sort()
print(A)
r = len(A)-1
l,mid=0,0
key = int(input("Enter the key :- "))
BSrecursive(A, key, l, r)