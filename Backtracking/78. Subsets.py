# Given an integer array nums of unique elements, return all possible subsets.
# The solution set must not contain duplicate subsets. Return the solution in any order.

nums = [1,2,3]

def subsets(): 
    n = len(nums)
    result = []
    curr_subset = []


    def backtrack(i): 
        if i == n: 
            result.append(curr_subset.copy())
            return

        curr_subset.append(nums[i])
        backtrack(i+1)
        curr_subset.pop()
        backtrack(i+1)

    backtrack(0)
    return result

print(subsets())
