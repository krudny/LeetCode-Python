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