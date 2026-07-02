def subsum(arr,idx,summ,s,target):
    #base condition 
    if idx == len(arr):
        if target == s:
            print(summ)
            return True
        else: 
            return False

    #calculation 
    summ.append(arr[idx])
    s += arr[idx]
    if subsum(arr, idx+1, summ, s,target) == True :
        return True
    s -= arr[idx]
    summ.pop()
    if subsum(arr, idx+1, summ, s,target) == True :
        return True
    return False
a=[1,2,1]
summ=[]
target = 3
subsum(a, 0, summ, 0,target)
# print(subsum(a, 0, summ, 0,target))
# print(sum(a))