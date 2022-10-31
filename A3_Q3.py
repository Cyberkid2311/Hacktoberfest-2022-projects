def gcd(A, B):
    if(A>B):
        x= A
        y= B
    else:
        x=B
        y = A

    while(y):
        x, y = y, x % y
    return x

A = 4
B = 6
print(gcd(A,B))