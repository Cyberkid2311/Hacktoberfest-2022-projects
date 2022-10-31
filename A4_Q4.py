def solve(A, B):
    ans = []
    n = len(A)
    flag = 0
    end = 0
    for i in range(0,n):
        if(A[i].startswith(B) and flag == 0):
            ans.append(i)
            flag = 1
            end = i
        elif(A[i].startswith(B)):
            end = i
    if(len(ans)==0):
        ans = [-1,-1]
    else:   
        ans.append(end)
    return ans


A = ['a', 'aa', 'aab', 'b', 'bb', 'bba', 'bbb']
B = 'bb'
print(solve(A,B))