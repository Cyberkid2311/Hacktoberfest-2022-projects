def solve(A):
    N = len(A)
    if (N % 2 == 0):
        return 0
    res = 0
    for i in range(0, N, 2):
        res ^= A[i]
    return res

A = [1, 2, 3]
print(solve(A))