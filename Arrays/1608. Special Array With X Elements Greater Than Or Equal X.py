from collections import Counter

# You are given an array nums of non-negative integers. 
# nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

nums = [0,4,3,0,4]

def specialArray(): 
    countedElements = Counter(nums)
    maxValue = max(countedElements)
    sumArray = [0] * (maxValue + 1)
    sumArray[maxValue] = countedElements[maxValue]

    for i in range(maxValue - 1, -1, -1): 
        sumArray[i] += sumArray[i + 1]
        if i in countedElements: 
            sumArray[i] += countedElements[i]

    for i in range(maxValue + 1): 
        if i == sumArray[i]: 
            return i

    return -1





print(specialArray())