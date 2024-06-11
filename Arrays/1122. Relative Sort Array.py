from collections import Counter
import heapq

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]

def relativeSort(arr1, arr2):
    m = len(arr2)
    i = 0
    count = Counter(arr1)
    res = [elem for elem in arr2 if elem in count for _ in range(count[elem])]
    heap = [elem for elem in arr1 if elem not in arr2]
    heapq.heapify(heap)

    while heap: 
        res.append(heapq.heappop(heap))

    return res

print(relativeSort(arr1, arr2))