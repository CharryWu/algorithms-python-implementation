# https://www.programiz.com/dsa/heap-data-structure
# https://www.educative.io/blog/data-structure-heaps-guide
"""
A heap is an advanced tree-based data structure used primarily for sorting and implementing priority queues.
They are complete binary trees that have the following features:

- Every level is filled except the leaf nodes (nodes without children are called leaves).
- Every node has a maximum of 2 children.
- All the nodes are as far left as possible, this means that every child is to the left of his parent.

Heaps are built based on the heap property, where any given node is
- always greater than its child nodes and the key of the root node is the largest among all other nodes. This property is also called max heap property.
- always smaller than the child nodes and the key of the root node is the smallest among all other nodes. This property is also called min heap property.
"""

"""
Heap API:
heapify: rearranges the elements in the heap to maintain the heap property.
insert: adds an item to a heap while maintaining its heap property.
delete: removes an item in a heap.
extract: returns the value of an item and then deletes it from the heap.
isEmpty: boolean, returns true if boolean is empty and false if it has a node.
size: returns the size of the heap.
getMax(): returns the maximum value in a heap
"""

from typing import Optional

class MaxHeap:
    """
    Elements in a max heap follow the max heap property.
    This means that the key at the parent node is always greater than the key at both child nodes.
    To build a max heap, you:
    - Create a new node at the beginning (root) of the heap.
    - Assign it a value.
    - Compare the value of the child node with the parent node.
    - Swap nodes if the value of the parent is less than that of either child (to the left or right).
    - Repeat until the largest element is at the root parent nodes (then you can say that the heap property holds).

    To remove/delete a root node in a Max Heap, you:
    - Delete the root node.
    - Move the last child node of the last level to root.
    - Compare the parent node with its children.
    - If the value of the parent is less than child nodes, swap them, and repeat until the heap property is satisfied.
    """
    def __init__(self, *args) -> None:
        if len(args) > 0 and isinstance(args[0], list):
            self.buildHeap(args[0])
        else:
            self.heap = []
            self.size = 0

    def __percolateUp(self, child_idx) -> None:
        """
        Restores the max heap property from a child node to a root node (parent > child).
        The __percolateUp() method is called recursively on each parent node until the root is reached.
        """
        parent_idx = (child_idx - 1) // 2
        if child_idx <= 0:
            return
        elif self.heap[parent_idx] < self.heap[child_idx]:
            self.heap[parent_idx], self.heap[child_idx] = self.heap[child_idx], self.heap[parent_idx]
            self.__percolateUp(parent_idx)

    def __maxHeapify(self, index) -> None:
        """
        Restores the max heap property from a specific node down to leaf nodes
        For every node to be positioned following the max-heap property,
        we call the __maxHeapify() method at every index of that array,
        starting from the bottom of the heap.
        """
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index

        if left < self.size and self.heap[largest] < self.heap[left]:
            largest = left
        if right < self.size and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.__maxHeapify(largest)

    def insert(self, val) -> None:
        """
        Appends a given value to the heap array and rearranges elements based on their heap property.
        On every new insert, the heap grows uniformly, and the size increases by one.
        """
        if self.size >= len(self.heap):
            self.size += 1
            self.heap.append(val)
            self.__percolateUp(len(self.heap)-1)
        else:
            self.heap[self.size] = val
            self.size += 1
            self.__percolateUp(self.size - 1)

    def getMax(self) -> Optional[int]:
        """
        Returns the maximum value in the heap (root node) without modifying the heap.
        Note that the time complexity here is constant time O(1)
        """
        if self.size > 0:
            return self.heap[0]
        return None

    def removeMax(self) -> Optional[int]:
        """
        Returns and removes the maximum value in the heap (think of pop()). The time complexity of this function is in O(log(n)).
        """
        maxval = self.heap[0]
        if self.size > 1:
            self.heap[0] = self.heap[self.size - 1]
            self.size = self.size - 1
            self.__maxHeapify(0)
            return maxval
        elif self.size == 1:
            self.size -= 1
            return maxval
        else:
            return None

    def buildHeap(self, arr) -> None:
        self.heap = list(arr)
        self.size = len(self.heap)

        for i in range(len(self.heap)-1, -1, -1):
            self.__maxHeapify(i)

if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.buildHeap([1,2,3,9,7,8])
    max_heap.insert(4)
    assert max_heap.removeMax() == 9
    assert max_heap.removeMax() == 8
    assert max_heap.removeMax() == 7
    max_heap.insert(6)
    max_heap.insert(5)
    assert max_heap.removeMax() == 6
    assert max_heap.removeMax() == 5
    assert max_heap.removeMax() == 4
    assert max_heap.removeMax() == 3
    assert max_heap.removeMax() == 2
    assert max_heap.removeMax() == 1