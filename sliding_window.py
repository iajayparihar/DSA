def max_sum(arr, k):
    window_sum = sum(arr[:k]) # from this we are creating window
    max_sum = window_sum # for getting max sum

    for i in range(k, len(arr)):
        first_element = arr[i-k]
        next_element = arr[i]
        window_sum = window_sum - first_element + next_element
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [2,1,5,1,3,2]

print(max_sum(arr,3))
#__________________________________
def pascal_triangle(n):
    row = [1]

    for _ in range(1, n + 1):
        new_row = [1]

        for j in range(1, len(row)):
            new_row.append(row[j - 1] + row[j])

        new_row.append(1)
        row = new_row
    return row

class Solution(object):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # First and last element are always 1.
        # Every middle element is the sum of the two elements above it.
        res = [1,1] # previous row
        for i in range(1,rowIndex+1):
            total = 0 # current total
            gen = []
            # gen.append(1) # first element
            for j in range(i-1):
                total = res[j] + res[j+1]
                gen.append(total)

            gen.append(1) # last element
            res = gen
        return gen
    
s = Solution()
print(s.getRow(5))
