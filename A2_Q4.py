def prime_fac(n):
    ans = []
    if(n<2):
        return ans
    i=2
    while(i<=n):
        while(n%i==0):
            n = n/i
            ans.append(i)
        i = i+1
    return ans

n = 56
print(prime_fac(n))