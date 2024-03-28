# Memoization => Top Down (Using recursion)
def fibMemo(n,memo):
    if n==1:
        return 0
    if n==2:
        return 1
    if n not in memo:
        memo[n]=fibMemo(n-1,memo)+fibMemo(n-2,memo)
    return memo[n]

print(fibMemo(6,{}))