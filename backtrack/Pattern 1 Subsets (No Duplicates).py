"""
Backtracking pattern: Subsets (No Duplicates)

Idea:
- At each index, make two choices: include the current number or skip it.
- This builds every subset of the input by exploring a binary decision tree.

Why it works:
- Every root-to-leaf path represents one unique subset.
- The recursion decides the inclusion of each element once, so all subsets are generated exactly once.

Time Complexity:
- There are 2^n possible subsets.
- Copying or storing one subset takes O(n) in the worst case.
- Total: O(n * 2^n)

Space Complexity:
- The recursion depth is O(n), and the current path also uses O(n).
- Extra space excluding output: O(n)
"""

nums = [1,2,3]

def backtrack(start, path):
    print(path)

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()

backtrack(0, [])