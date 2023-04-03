"""
Given two sorted arrays of size m and n respectively, you are tasked with finding
the element that would be at the kth position of the final sorted array.

Basic Approach
Since we are given two sorted arrays, we can use the merging technique to get
the final merged array. From this, we simply go to the kth index.
"""


def kth(arr1, arr2, m, n, k):
    """
    Program to find kth element
    from two sorted arrays
    """
    sorted1 = [0] * (m + n)
    i = 0
    j = 0
    d = 0
    while (i < m and j < n):

        if (arr1[i] < arr2[j]):
            sorted1[d] = arr1[i]
            i += 1
        else:
            sorted1[d] = arr2[j]
            j += 1
        d += 1

    while (i < m):
        sorted1[d] = arr1[i]
        d += 1
        i += 1
    while (j < n):
        sorted1[d] = arr2[j]
        d += 1
        j += 1
    return sorted1[k - 1]


# Driver code
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
print(kth(arr1, arr2, 5, 4, k))
