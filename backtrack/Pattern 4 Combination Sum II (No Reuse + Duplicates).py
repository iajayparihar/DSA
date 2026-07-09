"""
Backtracking pattern: Combination Sum II (No Reuse + Duplicates)

Idea:
- Similar to combination sum, but each number can be used at most once, and duplicates must be skipped.
- Sorting is used so equal values can be handled together.

Why it works:
- Each branch forms a unique combination that sums to the target.
- The duplicate-skip rule prevents the same combination from being generated multiple times.

Time Complexity:
- In the worst case, the search explores all subsets of the input, which is 2^n.
- Each branch may add a candidate to the current path.
- Total: O(2^n)

Space Complexity:
- The current combination and recursion stack use O(n) space.
- Extra space excluding output: O(n)
"""

nums = [10,1,2,7,6,1,5]
nums.sort()

def backtrack(start, target, path):
    if target == 0:
        print(path)
        return

    if target < 0:
        return

    for i in range(start, len(nums)):

        if i > start and nums[i] == nums[i-1]:
            continue

        path.append(nums[i])

        backtrack(i+1, target-nums[i], path)

        path.pop()

backtrack(0,8,[])