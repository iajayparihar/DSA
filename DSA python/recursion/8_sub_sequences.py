def subsequence(arr,idx,Earr):
    #base condition
    length=len(arr)
    if idx == length:
        print(Earr)
        return

    #add element in list
    Earr.append(arr[idx])
    #call fun +1 index
    subsequence(arr, idx+1, Earr)
    #remove element in list
    Earr.pop()
    # # call for +1 index
    subsequence(arr, idx+1, Earr)

a=[3,1,2]
Earr=[]
subsequence(a, 0, Earr)
