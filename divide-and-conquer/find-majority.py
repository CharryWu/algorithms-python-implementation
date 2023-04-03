"""
You are given an array of n objects, A[1]…A[n]. You are allowed to compare whether
two objects are equal (A[i] == A[j]) but there is no ordering on the objects,
i.e. you cannot sort them.  An element of A is called the majority if it occurs at least (n/2 + 1) times.

Design a divide & conquer algorithm that return either returns the majority element
and the number of times it appears, or returns null if there is no majority element.
To receive full credit your algorithm should run in time O(nlogn).
For simplicity, you may assume that n is a power of two.

Majority (A, i, j)
    If (i = j) return (A[i], 1)
    (L_ele, L_count) = majority(A, i, (i+j-1)/2 )
    (R_ele, R_count) = majority(A, (i+j+1)/2, j)

    If (L_ele != null)
        For k = ((i+j+1) / 2) to j
            If A[k] == L_ele then L_count++
        If L_count > (j-i+1)/2 return (L_ele, L_count)

    If (R_ele != null)
        For k = i to (i+j–1) /2
            If A[k] == R_ele then R_count++
        If R_count > (j-i+1)/2 return (R_ele, R_count)

    Return null

Since the overall majority must be the majority of either the left or right halves,
we get these, count their occurrences in the whole array, and return if either is a majority.
This requires O(N) time, plus the time for the two recursive calls.
"""