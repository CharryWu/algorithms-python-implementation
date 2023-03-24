"""
The heapsort algorithm starts by using BUILD-MAX-HEAP to build a max-heap
on the input array A. Since the maximum element of the array is stored at the root A[0],
we can put it into its correct final position by exchanging it with A[n-1].
If we now discard node n from the heap—and we
can do so by simply decrementing A.heap-size. We observe that the children of
the root remain max-heaps, but the new root element might violate the max-heap
property. All we need to do to restore the max-heap property, however, is call
MAX-HEAPIFY(A, 0), which leaves a max-heap in A[:n-1]. The heapsort
algorithm then repeats this process for the max-heap of size n-1 down to a heap
of size 2.
"""
# Heap Sort in python

def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def buildMaxHeap(arr, n):
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

def heapSort(arr):
    """
    Time Complexity: O(nlogn). Call to buildMaxHeap takes O(n), each n-1 call to heapify takes O(logn)
    """
    n = len(arr)
    buildMaxHeap(arr, n)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [1,12,9,5,6,10]
    heapSort(arr)
    assert arr == [1,5,6,9,10,12]
