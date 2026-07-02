# n a binary Search aRRaay must be Sorted
A=[12,15,20,25,26,39,41,51,53,59,62,71,1]
# A=[1,12,15,20,25,26,39,41,51,53,59,62,71]
print(A)
A.sort()
print("Sorted Array",A)
key=int(input("Enter the num you want search in Array= "))
l=0 
r=len(A)-1
mid=0
while (l<=r):        #when A[l] cross A[r] 
    mid=(l+r)//2        
    if key==A[mid]:     
        print(" key is at index=",mid) 
        break
    elif key<A[mid]:   
        r=mid-1
    else:
        l=mid+1
else:
    print("key is not in Array")