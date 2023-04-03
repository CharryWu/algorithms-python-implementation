"""
Quickselect is a selection algorithm to find the k-th smallest element in an unordered list.
It is related to the quick sort sorting algorithm.

The algorithm is similar to QuickSort. The difference is, instead of recurring
for both sides (after finding pivot), it recurs only for the part that contains
the k-th smallest element. The logic is simple, if index of the partitioned
element is more than k, then we recur for the left part.
If index is the same as k, we have found the k-th smallest element and we return.
If index is less than k, then we recur for the right part. This reduces the
expected complexity from O(n log n) to O(n), with a worst-case of O(n^2).

Pseudocode:
function quickSelect(list, left, right, k)
   if left = right
      return list[left]

   Select a pivotIndex between left and right

   pivotIndex := partition(list, left, right, pivotIndex)
   if k = pivotIndex
      return list[k]
   else if k < pivotIndex
      right := pivotIndex - 1
   else
      left := pivotIndex + 1
"""
# https://www.geeksforgeeks.org/quickselect-algorithm/
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# https://leetcode.com/problems/top-k-frequent-elements/
# https://leetcode.com/problems/k-closest-points-to-origin/
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
# Python3 program of Quick Select

def partition(arr, l, r):
    """
    Standard partition process of QuickSort().
    It considers the last element as pivot
    and moves all smaller element to left of
    it and greater elements to right
    """
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k):
    """
    finds the kth position (of the sorted array)
    in a given unsorted array i.e this function
    can be used to find both kth largest and
    kth smallest element in the array.
    ASSUMPTION: all elements in arr[] are distinct
    """
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if (index - l == k - 1):
            return arr[index]

        # If position is more, recur
        # for left subarray
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, index + 1, r, k - index + l - 1)
    print("Index out of bound")


# Driver Code
arr = [10, 4, 5, 8, 6, 11, 26]
n = len(arr)
k = 3
print("K-th smallest element is ", end="")
print(kthSmallest(arr, 0, n - 1, k)) # K-th smallest element is 6
