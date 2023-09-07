# algorithms-python-implementation
A Python implementation of algorithms and data structures mentioned in CLRS textbook

Each file contains the implementation of a single algorithm and data structure,
optionally followed by driver code and 1~2 test cases.

All words in file names are concatenated by hyphens `-`, and you can run each single
file with no problem. But python pakcage import doesn't allow the dash character,
so make your own copy when you'd like to use code from this repo.

If an algorithm or data structure belongs to multiple categories, multiple copies
of that algo or DS will exist in this repo.

## Folder Structure
- `divide-and-conquer`
    - merge sort and quick sort
    - binary search (or algorithms based on binary seaerch)
- `dynamic-programming`
    - longest ... sequence/substring
- `graph`
    - cycle
    - connected components
    - shortest paths
    - MST
    - network flow
    - other class graph algorithms
- `greedy`
    - LRU cache
    - activity scheduling
    - ...
- `heap`
    - max heap
    - min heap
- `sorting`
    - classic O(N^2) and O(NlogN) sorting algorithms
- `state-machine`
    - numeric string parsing
- `clustering`
    - K-means
