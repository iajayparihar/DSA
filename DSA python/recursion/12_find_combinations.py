def unique(arr,target,s,idx,earr):

    # base condition 
    if idx == len(arr):
        if target == 0:
            # s.append(earr)
            s+=tuple(earr)
            print(s)
        return
    if target >= arr[idx]:
        earr.append(arr[idx])
        unique(arr, target-arr[idx], s, idx, earr)
        earr.pop()
    
    unique(arr, target, s, idx+1, earr)
    # return s
a=[2,3,6,7]
targ=10
indx=0
earr=[]
s=()
a=unique(a, targ,s,indx, earr)
print(a)