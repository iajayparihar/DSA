def permu(arr,index,ans):
    if index >= len(arr)-1:
        ans.append(arr)
        return
    
    for i in range(index,len(arr)):
        arr[i],arr[index]=arr[index],arr[i]
        permu(arr.copy(), index+1, ans)
        # backtracking
        arr[i],arr[index]=arr[index],arr[i]

arr=[1,2,3]
index=0
ans=[]
permu(arr, index, ans)
print(ans)
print(len(ans))