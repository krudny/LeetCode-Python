# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
# Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

def wordBreak(): 
    n = len(s)
    result = []

    def dfs(i, j, splitted_array):
        if i == n:
            if len(splitted_array) == 0 or j != n: 
                return
            for word in splitted_array: 
                if word not in wordDict: 
                    return 
            result.append(splitted_array)
            return


        dfs(i+1, j, splitted_array)
        dfs(i+1, i+1, splitted_array + [s[j:i+1]])


    dfs(0, 0, [])
    for i in range(len(result)):
        result[i] = ' '.join(result[i])

    return result

    


print(wordBreak())
