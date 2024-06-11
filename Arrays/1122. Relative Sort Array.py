# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
# Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

from collections import Counter
import heapq

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]

def relativeSort(arr1, arr2):
    count = Counter(arr1)
    res = [elem for elem in arr2 for _ in range(count[elem])]
    heap = [elem for elem in arr1 if elem not in arr2]
    heapq.heapify(heap)

    while heap: 
        res.append(heapq.heappop(heap))

    return res

print(relativeSort(arr1, arr2))