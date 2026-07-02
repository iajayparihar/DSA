def combination(arr,idx,target,s,Earr):
    #base condition
    if idx == len(arr):
        if target == 0:
            s.add(tuple(Earr))
        return 
        # print(s)

    for i in range(len(arr)): # mistake in loop 

        if i > idx and arr[i]==arr[i-1]:
            continue
        if target < arr[i]:
            break

        Earr.append(arr[i])
        combination(arr, i+1, target-arr[i], s, Earr)
        Earr.pop()
    
    return s


candidates=[10,1,2,7,6,1,5]
tar = 8
indx=0
candidates.sort()
print("sorted list :- ",candidates)
s=set()
earr=list()
a=combination(candidates, indx, tar, s,earr)
print(a)