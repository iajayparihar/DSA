def diagonalDifference(arr):
    # Write your code here
    fdig=0
    sdig=0
    length=len(arr)-1
    print(length)
    for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         # if i==j :
    #         pass
    #         #     fdig+=arr[i][j]  
    # # for i in range(len(arr)):
        for k in range(length,-1,-1):
            if i+k== length:
                sdig+=arr[i][k]
                                        
    cal=fdig-sdig
    if cal<0:
        cal=-(cal)
        return cal
    return cal
    

a=diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]])
print(a)