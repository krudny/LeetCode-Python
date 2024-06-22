pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]

def findLongestChain():
    n = len(pairs)
    pairs.sort()
    dp = [1] * n

    dp[0] = 1

    for i in range(1, n): 
        for j in range(i, -1, -1): 
            if pairs[i][0] > pairs[j][1]: 
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[-1]

    


print(findLongestChain())