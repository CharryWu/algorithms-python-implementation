"""
Given corrupted document with no punctuation, can you reconstruct it as a sequence of valid words (with aid of a dictionary)?
“tomatomiced” = tom | atom | iced
“catchaserat” = cat | chase | rat
“afarfarbetterthing” = ?
Input:
Corrupted document x[1:n] (array of characters)
Dictionary function dict(w) (returns true if w is a valid word)

Subproblem
    T(k)    = true if x[1:k] is a valid sequence of words
               = false, otherwise
We want T(n)
Given T(1), …, T(k-1), how do we figure out T(k)?
  T(k) = true iff there is some  such that
      T(j-1) is true AND
      x[j:k] is a valid word
Define T(0) = true for consistency
Instead of solving recursively, tabulate or memoize to avoid redundant calculations
"""

def stringReconstruction(s, dict):
    n = len(s)
    T = [False] * (n+1)
    T[0] = True
    D = [0] * n # To reconstruct the document, use additional array D[n]
    for i in range(1, n+1):
        for j in range(i):
            if T[j] and s[j:i] in dict:
                T[i] = True
                D[i-1] = j
    # If T(k) = true then D(k) = starting position of the word that ends at x[k] reconstruct by following backpointers
    if T[n]:
        res = []
        start, end = n-1, n
        while start >= 0:
            if T[start]:
                res.append(s[start:end])
                end = start
            start -= 1
        res.reverse()
        return res
    else:
        return []

if __name__ == '__main__':
    assert stringReconstruction("tomatomiced", set(['tom', 'atom', 'iced'])) == ['tom', 'atom', 'iced']

