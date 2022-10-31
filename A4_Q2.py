import math
def power(x):
    if x == 0:
        return False
 
    return (math.log10(x) /
            math.log10(2))
 
def isPowerOfTwo(n):
    return (math.ceil(power(n)) ==
            math.floor(power(n)))
 
num = 8
ans = isPowerOfTwo(num)
if(ans):
    print("Yes")
else:
    print("No")