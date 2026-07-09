"""
Backtracking pattern: Subsets II (Duplicates)

Idea:
- This is the same as subsets, but duplicates must be avoided by skipping equal elements at the same level.
- Sorting helps identify duplicate values and prevents repeated subsets.

Why it works:
- Each valid path represents one unique subset.
- The skip rule ensures duplicate values are not used in the same combination position more than once.

Time Complexity:
- The number of distinct subsets is still at most 2^n.
- Each subset may need O(n) time to build or copy.
- Total: O(n * 2^n)

Space Complexity:
- Recursion depth and the current subset both require O(n) space.
- Extra space excluding output: O(n)
"""


def backtrack(start, path):
    print(path)

    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:
            continue

        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()

nums = [1,2,2]
nums.sort()
backtrack(0, [])

# []
# [1]
# [1, 2]
# [1, 2, 2]
# [2]
# [2, 2]