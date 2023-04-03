"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm.
It picks an element as a pivot and partitions the given array around the picked pivot.
There are many different versions of quickSort that pick pivot in different ways.

- Always pick the first element as a pivot.
- Always pick the last element as a pivot (implemented below)
- Pick a random element as a pivot.
- Pick median as the pivot.

The key process in quickSort is a partition(). The target of partitions is,
given an array and an element x of an array as the pivot, put x at its correct
position in a sorted array and put all smaller elements (smaller than x) before x,
and put all greater elements (greater than x) after x.
All this should be done in linear time.
"""

def partition(A, low, high):
    """
    There can be many ways to do partition, following pseudo-code adopts the
    method given in the CLRS book. The logic is simple, we start from the leftmost
    element and keep track of the index of smaller (or equal to) elements as i.

    While traversing, if we find a smaller element, we swap the current element with arr[i].
    Otherwise, we ignore the current element.

    You may view the input array as divided into four regions:
    LOW | HIGH | UNSORTED | PIVOT
    Initially both LOW and HIGH subarray are empty
    Each iteration consider one element from UNSORTED, moving it either to HIGH or LOW
    UNSORTED occupies A[low..high-1], PIVOT always stays at A[high]
    Each loop grows LOW and HIGH by one element per iteration
    """
    # Choose the rightmost element as pivot
    pivot = A[high]
    # Pointer for greater element
    i = low-1
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if A[j] <= pivot: # if A[j] > pivot, it automatically goes to HIGH, no need to swap
            # If element smaller than pivot is found swap it with the greater element pointed by i.
            # This moves the A[i] to HIGH, A[j] to LOW
            i += 1
            # Swapping element at i with element at j
            A[i], A[j] = A[j], A[i]
    # Swap the pivot element to the correct position: the greater element specified by i
    A[i+1], A[high] = A[high], A[i+1]
    # Return the position from where partition is done
    return i+1

def quickSort(A, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        partition_i = partition(A, low, high)
        quickSort(A, low, partition_i-1) # Recursive call on the left of pivot
        quickSort(A, partition_i+1, high) # Recursive call on the right of pivot

A = [10, 7, 8, 9, 1, 5]
quickSort(A, 0, len(A)-1)
print(f'Sorted Array: {A}')