def max_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        first_element = arr[i-k]
        next_element = arr[i]
        window_sum = window_sum - first_element + next_element
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [2,1,5,1,3,2]
print(max_sum(arr,3))