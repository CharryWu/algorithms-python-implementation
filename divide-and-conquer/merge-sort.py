"""
Merge sort is defined as a sorting algorithm that works by dividing an array
into smaller subarrays, sorting each subarray, and then merging the sorted
subarrays back together to form the final sorted array.

In simple terms, we can say that the process of merge sort is to divide the
array into two halves, sort each half, and then merge the sorted halves back
together. This process is repeated until the entire array is sorted.

MergeSort has a guaranteed time complexity of O(nlogn)
"""
# Related LeetCode problem: https://leetcode.com/tag/merge-sort/
def merge(arr1, arr2):
    """
    merge two sorted arr1 and arr2 into a new sorted array
    """
    n1, n2 = len(arr1), len(arr2)
    merged = [0] * (n1+n2)
    i, j, k = 0, 0, 0

    # write to merged array, select the smaller element from arr1 or arr2 at one time
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        merged[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        merged[k] = arr2[j]
        j += 1
        k += 1

    return merged

def mergeSort(arr):
    n = len(arr)
    if n == 1: # base case: only one element in array, no need to merge
        return arr
    mid = n//2

    sorted_first_half = mergeSort(arr[:mid])
    sorted_second_half = mergeSort(arr[mid:])

    return merge(sorted_first_half, sorted_second_half)

arr = [3, 6, 5, 2, 7, 9]
assert mergeSort(arr) == [2, 3, 5, 6, 7, 9]
