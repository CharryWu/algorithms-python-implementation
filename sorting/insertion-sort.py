# Related LeetCode problem: https://leetcode.com/problems/insertion-sort-list/
def insertionSort(arr):
    """
    Basic idea:
    n keys are in array A[1:n]
    assume A[1:j-1] are sorted
    for A[j]: compared against A[1:j-1] & inserted in right place
    """
    n = len(arr)
    for i in range(n):
        cur = arr[i]
        found_j = i
        for j in range(i+1, n):
            if arr[j] < cur:
                cur = arr[j]
                found_j = j
        # swap found element to correct posision i
        arr[i], arr[found_j] = arr[found_j], arr[i]

    return arr


# Driver code
arr = [3, 6, 5, 2, 7, 9]
assert insertionSort(arr) == [2, 3, 5, 6, 7, 9]
