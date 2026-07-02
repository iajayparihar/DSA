def subsum(arr,idx,s,target):
    #base condition
    if idx == len(arr):
        if target == s: 
            return 1
        else : 
            return 0

    #calculation 
    s += arr[idx]
    l = subsum(arr, idx+1, s,target)
    s -= arr[idx]
    r = subsum(arr, idx+1, s,target)
    return l+r
a=[1,2,1]

target = 2
a=subsum(a, 0, 0,target)
print("The occurence of no is:-",a)
