def segregate_positive_negative(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        if arr[left] > 0:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1

    return arr

# Example 1:
arr1 = [1, -1, 3, 2, -7, -5, 11, 6]
result1 = segregate_positive_negative(arr1)
print(result1)
