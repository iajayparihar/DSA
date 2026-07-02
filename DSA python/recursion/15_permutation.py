
def permutation(idx,arr,ans):
    if idx == len(arr):
        ans.add(tuple(arr))
        return
    
    for i in range(len(arr)):
        arr[i],arr[idx]=arr[idx],arr[i]
        permutation(idx+1, arr, ans)
        arr[i],arr[idx]=arr[idx],arr[i]
    

a=[1,2,3]
ans = set() # we don't need the duplicate element in ans
k=permutation(0, a, ans)
print(ans)