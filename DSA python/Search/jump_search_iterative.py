def jump_search(arr,key,i):
    length=len(arr)-1 # pointing last element of array
    last = arr[length]
    if key <= last:
        while (i<=length and arr[i] < key) :
            if key == arr[i]:
                print("the key found in ",i, "Index")
                break
            i+=4
    #  this is used for find the subset of element...  
        if key == arr[i]:
            print("the key found in ",i, "Index")
        elif key == arr[i-1]:
            print("the key found in ",i-1, "Index")
        elif key == arr[i-2]:
            print("the key found in ",i-2, "Index")
        elif key == arr[i-3]:
            print("the key found in ",i-3, "Index")
        else:
            print("key not found in Array")
    else :
        print("Key is not found in Array ")    
"""------------------------------------

        for j in range(i,-1,-1):
            if key == arr[j]:
                print("the key found in ",j, "Index")
                break
    else :
        print("Key is not found in Array ")    

------------------------------------"""
# in jump search array must be sorted 
A=[12,15,20,25,26,39,41,51,53,59,62,71,1]
A.sort()

print("the Array is := ",A)
targ = int(input("Enter key for searching:- "))

jump_search(A, targ, 0)
