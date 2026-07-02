def subsum(arr,idx,summ,s,target):
    #base condition 
    if idx == len(arr):
        if target == s:
            print(summ)
        return

    #calculation 
    summ.append(arr[idx])
    s += arr[idx]
    subsum(arr, idx+1, summ, s,target)
    s -= arr[idx]
    summ.pop()
    subsum(arr, idx+1, summ, s,target)

a=[1,2,1]
summ=[]
target = 2
subsum(a, 0, summ, 0,target)
# print(sum(a))