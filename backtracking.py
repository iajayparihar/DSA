arr = [1,2]
res = []
def backtrack(start, path):
    res.append(path[:])
    ##conditions
    # if start == len(arr):
    #     return
    for i in range(start, len(arr)):
        path.append(arr[i])
        backtrack(i + 1, path)
        path.pop()

backtrack(0, [])
print(res)