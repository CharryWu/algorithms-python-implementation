import random

def partition(A, low, high):
    """
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

def partitionRandom(A, low, high):
    randpivot = random.randrange(low, high)
    A[high], A[randpivot] = A[randpivot], A[high]
    return partition(A, low, high)

def quickSortRandom(A, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        partition_i = partitionRandom(A, low, high)
        quickSortRandom(A, low, partition_i-1) # Recursive call on the left of pivot
        quickSortRandom(A, partition_i+1, high) # Recursive call on the right of pivot

A = [10, 7, 8, 9, 1, 5]
quickSortRandom(A, 0, len(A)-1)
print(f'Sorted Array: {A}')