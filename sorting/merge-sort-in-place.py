# Related LeetCode problem: https://leetcode.com/tag/merge-sort/
# In-place index-based implementation, saves space of creating copies of input arr
def merge(arr, s1, e1, s2, e2):
    """
    merge sorted array subranges [s1,e1) and [s2,e2) using in-place modification
    it assumes e1==s2, write data back to [s1, e2)
    see https://leetcode.com/problems/merge-sorted-array/description/
    and https://leetcode.com/problems/merge-two-sorted-lists/
    """
    assert 0 <= s1 < e1 <= s2 < e2 <= len(arr)
    if arr[e1-1] <= arr[s2]: # shortcut: arr[s1:e2] is already sorted
        return

    # write the result from back to front, doing it this way can prevent
    # meddling with data that's already written to the front
    while s1 < e1 and s2 < e2:
        if arr[s1] <= arr[s2]: # If element from arr1 is in right place, pass
            s1 += 1
        else: # Need to move element from arr2 to front
            val = arr[s2]
            index = s2

            # Shift all the elements between arr[s1] and arr[s2] right by 1.
            while index != s1:
                arr[index] = arr[index-1]
                index -= 1

            arr[s1] = val # put element from arr2 into right place

            # Update all the pointers
            s1 += 1
            e1 += 1
            s2 += 1

def mergeSort(arr, begin=0, end=None):
    """
    sort array range [begin, end)
    """
    if end is None:
        end = len(arr)
    assert begin >= 0 and end <= len(arr)
    n = end-begin
    if n <= 1: # base case: only one element in array, no need to merge
        return
    mid = (end+begin)//2

    mergeSort(arr, begin, mid)
    mergeSort(arr, mid, end)

    merge(arr, begin, mid, mid, end)

arr = [3, 6, 5, 2, 7, 9]
mergeSort(arr)
assert  arr == [2, 3, 5, 6, 7, 9]
