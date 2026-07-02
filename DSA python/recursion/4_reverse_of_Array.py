def RArr(arr,i):
    n=len(arr)
    y= n-i-1        # pointing to the last element
    # base condition 
    if i >= n/2 :
        print(arr)
        return
    #swap
    arr[i],arr[y] = arr[y],arr[i]

    #funcion call
    RArr(arr,i+1)
    
a=[1,2,3,4,5]
RArr(a,0)



# def RArr(arr,l,r):
#     # base condition 
#     if l >= r :
#         print(arr)
#         return 
    
#     #swap
#     arr[l],arr[r] = arr[r],arr[l]

#     #funcion call
#     RArr(arr, l+1, r-1)
    

# a=[1,2,3,4,5]
# right = len(a) - 1
# left=0

# print("ihsjud",RArr(a, left, right))
