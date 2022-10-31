def merge(A, n1, B, n2):
    ans = []
    i=0
    j=0
    while(i<n1 and j<n2):
        if(A[i]<=B[j]):
            ans.append(A[i])
            i=i+1
        else:
            ans.append(B[j])
            j=j+1
    
    if(i!=n1):
        while(i<n1):
            ans.append(A[i])
            i=i+1
    if(j!=n2):
        while(j<n2):
            ans.append(B[j])
            j=j+1
    return ans

A = [-1,2,4]
n1 = 3
B= [-1,-1,1,3,5]
n2 = 5  

print(merge(A,n1,B,n2))