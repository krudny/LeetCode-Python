# You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.
# You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
# You need to assign each city with an integer value from 1 to n, where each value can only be used once. 
# The importance of a road is then defined as the sum of the values of the two cities it connects.
# Return the maximum total importance of all roads possible after assigning the values optimally.



n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]

def maximumImportance(n, roads): 
    edges = [0] * n

    for u, v in roads: 
        edges[u] += 1
        edges[v] += 1

    label = 1
    res = 0

    for count in sorted(edges): 
        res += label * count
        label += 1

    return res

print(maximumImportance(n, roads))