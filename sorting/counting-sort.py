"""
Counting sort assumes that each of the n input elements is an integer in the range
0 to k, for some integer k. When k = O(n), the sort runs in O(n) time.

Counting sort determines, for each input element x, the number of elements less
than x. It uses this information to place element x directly into its position in the
output array
"""

def countingSort(A, k):
    """
    A: input array to be sorted, 0<=A[i]<=k
    k: upper bound of element value in A
    """
    n = len(A)
    C = [0] * (k+1)
    output = [0] * n

    for j in range(n):
        C[A[j]] += 1
    # Postcond: C contains frequencies of all elements in A
    for i in range(1, k+1):
        C[i] += C[i-1]
    # Postcond: C now contains the number of elements less than or equal to i
    for j in range(n-1, -1, -1):
        val = A[j]
        valpos = C[val]-1
        output[valpos] = val
        C[val] -= 1
    return output

if __name__ == '__main__':
    print(countingSort([2,5,3,0,2,3,0,3], 5))