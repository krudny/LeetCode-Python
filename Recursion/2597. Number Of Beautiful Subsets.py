# You are given an array nums of positive integers and a positive integer k.
# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
# Return the number of non-empty beautiful subsets of the array nums.
# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. 
# Two subsets are different if and only if the chosen indices to delete are different.

nums = [10,4,5,7,2,1]
k = 3

def beautifulSubsets(nums, k): 
    n = len(nums)

    def dfs(i, subset): 
        if i == n: 
            return 1 if len(subset) != 0 else 0
        
        res = 0
        if nums[i] - k not in subset and nums[i] + k not in subset: 
            res = dfs(i + 1, subset + [nums[i]]) 

        res += dfs(i + 1, subset)
        return res
        

    return dfs(0, [])


print(beautifulSubsets(nums, k))