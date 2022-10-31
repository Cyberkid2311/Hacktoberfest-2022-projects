def solve(A):
    B = set(A)
    C = list(B)
    C.sort()
    if(len(C) == 1):
        return 0
    else:
        return C[-2]%C[-1]

A = [1, 2, 44, 3]
print(solve(A))