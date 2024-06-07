# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering

from collections import Counter

s = "leetcode"
t = "practice"

def minSteps(s, t): 
    count = Counter(t)
    res = 0

    for i in range(len(s)): 
        if count[s[i]] > 0: 
            count[s[i]] -= 1
        else: 
            res += 1

    return res
    
print(minSteps(s, t))