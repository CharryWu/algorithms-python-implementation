"""
Implement a function convertMax(maxHeap) which will convert a binary max heap
into a binary min heap where maxHeap is an array in the maxHeap format
(i.e. the parent is greater than its children). Your output should be a converted array.
"""

from typing import List

def minHeapify(heap: List[int], index: int):
    left = index * 2
    right = (index * 2) + 1
    smallest = index

    if left < len(heap) and heap[smallest] > heap[left]:
        smallest = left

    if right < len(heap) and heap[smallest] > heap[right]:
        smallest = right

    if smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        minHeapify(heap, smallest)

    return heap

def convertMax(maxHeap):
    for i in range(len(maxHeap)//2, -1, -1):
        maxHeap = minHeapify(maxHeap, i)
    return maxHeap

if __name__ == '__main__':
    maxHeap = [9,4,7,1,-2,6,5]
    assert convertMax(maxHeap) == [-2, 1, 4, 5, 7, 6, 9]