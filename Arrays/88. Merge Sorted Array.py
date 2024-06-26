# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3



def merge(nums1, nums2, m, n): 
    a, b, correct_index = m - 1, n - 1, m + n - 1

    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[correct_index] = nums1[a]
            a -= 1
        else:
            nums1[correct_index] = nums2[b]
            b -= 1

        correct_index -= 1

    
merge(nums1, nums2, m, n)