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
    """
    Find largest among root and children (but not its subtreets).
    If the largest isn't the root, but one of its two children,
    then the heap property has been violated. In this case, we move the largest
    up to the root (restore heap property). Since a smaller element has been swapped to
    the original child position with largest value,
    we continue the recursive call on the child position
    """
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def buildMaxHeap(arr, n):
    """
    Build max heap. Only need to heapify on the first n elements
    (since all of their children will be checked)
    """
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

def heapSort(arr):
    """
    Time Complexity: O(nlogn). Call to buildMaxHeap takes O(n), each n-1 call to heapify takes O(logn)
    """
    n = len(arr)
    buildMaxHeap(arr, n)

    # precondition: max element of arr[0..i] at arr 0th index, swap
    # it to correct index i.
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element. Here we only check root and two of its children
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [1,12,9,5,6,10]
    heapSort(arr)
    assert arr == [1,5,6,9,10,12]
