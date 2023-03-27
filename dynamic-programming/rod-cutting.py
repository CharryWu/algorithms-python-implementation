def cutRod(price, n):
    memo = {}
    def dfs(l):
        if l == 0:
            return 0
        if l in memo:
            return memo[l]

        profit_l = float('-inf')
        for cut in range(1, l+1):
            profit_l = max(profit_l, price[cut-1]+cutRod(price, l-cut))
        memo[l] = profit_l
        return profit_l

    return dfs(n)

print(cutRod([1,5,8,9,10,17,17,20,24,30], 4)) # Output: 10

def cutRodBottomUp(price, n):
    revenue = [0] * (n+1)
    for l in range(1, n+1):
        profit_l = float('-inf')
        for cut in range(1,l+1):
            profit_l = max(profit_l, price[cut-1]+revenue[l-cut])
        revenue[l] = profit_l
    return revenue[n]

print(cutRodBottomUp([1,5,8,9,10,17,17,20,24,30], 4)) # Output: 10

def cutRodBottomUpWithSolution(price, n):
    revenue = [0] * (n+1)
    solution = [0] * (n+1)
    for l in range(1, n+1):
        profit_l = float('-inf')
        for cut in range(1,l+1):
            profit_candidate = price[cut-1] + revenue[l-cut]
            if profit_l < profit_candidate:
                profit_l = profit_candidate
                solution[l] = cut
        revenue[l] = profit_l
    return revenue[n], solution

def printSolution(price, n):
    r, s = cutRodBottomUpWithSolution(price, n)
    print("Max revenue is", r)

    while n > 0:
        print(s[n])
        n -= s[n]

printSolution([1,5,8,9,10,17,17,20,24,30], 7) # 1 and 6

