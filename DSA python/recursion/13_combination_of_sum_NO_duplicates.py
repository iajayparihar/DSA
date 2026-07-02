def combination(arr,idx,target,s,Earr):
    #base condition
    if idx == len(arr):
        if target == 0:
            s.add(tuple(Earr))
            # print(s)
        return

    if target >= arr[idx]:
        Earr.append(arr[idx])
        combination(arr, idx+1, target-arr[idx], s, Earr)
        Earr.pop()
    combination(arr, idx+1, target, s, Earr)
    return s
    
candidates=[10,1,2,7,6,1,5]
tar = 8
indx=0
s=set()
candidates.sort()
print("sorted list :- ",candidates)
earr=list()
a=combination(candidates, indx, tar, s,earr)
print(a)