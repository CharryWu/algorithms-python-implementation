# https://www.programiz.com/dsa/heap-data-structure
# https://www.educative.io/blog/data-structure-heaps-guide
"""
A heap is an advanced tree-based data structure used primarily for sorting and implementing priority queues.
They are complete binary trees that have the following features:

- Every level is filled except the leaf nodes (nodes without children are called leaves).
- Every node has a maximum of 2 children.
- All the nodes are as far left as possible, this means that every child is to the left of his parent.

Heaps are built based on the heap property, where any given node is
- max heap: always greater than its child nodes and the key of the root node is the largest among all other nodes.
- min heap: always smaller than the child nodes and the key of the root node is the smallest among all other nodes.
"""

"""
Heap API:
heapify: rearranges the elements in the heap to maintain the heap property.
insert: adds an item to a heap while maintaining its heap property.
delete: removes an item in a heap.
extract: returns the value of an item and then deletes it from the heap.
isEmpty: boolean, returns true if boolean is empty and false if it has a node.
size: returns the size of the heap.
getMin(): returns the minimum value in a heap
"""

from typing import Optional

class MinHeap:
    """
    Elements in a min heap follow the min heap property.
    This means that the key at the parent node is always smaller than the key at both child nodes.
    To build a min heap, you:
    - Create a new node at the beginning (root) of the heap.
    - Assign it a value.
    - Compare the value of the child node with the parent node.
    - Swap nodes if the value of the parent is greater than that of either child (to the left or right).
    - Repeat until the smallest element is at the root parent nodes (then you can say that the heap property holds).

    To remove/delete a root node in a min Heap, you:
    - Delete the root node.
    - Move the last child node of the last level to root.
    - Compare the parent node with its children.
    - If the value of the parent is greater than child nodes, swap them, and repeat until the heap property is satisfied.
    """
    def __init__(self, *args) -> None:
        if len(args) > 0 and isinstance(args[0], list):
            self.buildHeap(args[0])
        else:
            self.heap = []
            self.size = 0

    def __percolateUp(self, child_idx) -> None:
        """
        Restores the min heap property from a child node to a root node (parent > child).
        The __percolateUp() method is called recursively on each parent node until the root is reached.
        """
        parent_idx = (child_idx - 1) // 2
        if child_idx <= 0:
            return
        elif self.heap[parent_idx] > self.heap[child_idx]:
            self.heap[parent_idx], self.heap[child_idx] = self.heap[child_idx], self.heap[parent_idx]
            self.__percolateUp(parent_idx)

    def __minHeapify(self, index) -> None:
        """
        Restores the min heap property from a specific node down to leaf nodes
        For every node to be positioned following the min-heap property,
        we call the __minHeapify() method at every index of that array,
        starting from the bottom of the heap.

        heapify(array):
            Root = array[0]
            Largest = largest( array[0] , array [2*0 + 1]. array[2*0+2])
            if(Root != Largest)
                Swap(Root, Largest)
        """
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index

        if left < self.size and self.heap[smallest] > self.heap[left]:
            smallest = left
        if right < self.size and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.__minHeapify(smallest)

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

    def getMin(self) -> Optional[int]:
        """
        Returns the minimum value in the heap (root node) without modifying the heap.
        Note that the time complexity here is constant time O(1)
        """
        if self.size > 0:
            return self.heap[0]
        return None

    def removeMin(self) -> Optional[int]:
        """
        Returns and removes the minimum value in the heap (think of pop()). The time complexity of this function is in O(log(n)).
        """
        minval = self.heap[0]
        if self.size > 1:
            self.heap[0] = self.heap[self.size - 1]
            self.size -= 1
            self.__minHeapify(0)
            return minval
        elif self.size == 1:
            self.size -= 1
            return minval
        else:
            return None

    def buildHeap(self, arr) -> None:
        self.heap = list(arr)
        self.size = len(arr)

        for i in range(len(arr)//2, -1, -1):
            self.__minHeapify(i)

if __name__ == '__main__':
    min_heap = MinHeap([8,7,9,3,2,1])
    min_heap.insert(4)
    assert min_heap.removeMin() == 1
    assert min_heap.removeMin() == 2
    assert min_heap.removeMin() == 3
    min_heap.insert(6)
    min_heap.insert(5)
    assert min_heap.removeMin() == 4
    assert min_heap.removeMin() == 5
    assert min_heap.removeMin() == 6
    assert min_heap.removeMin() == 7
    assert min_heap.removeMin() == 8
    assert min_heap.removeMin() == 9