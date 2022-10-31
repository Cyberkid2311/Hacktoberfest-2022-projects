class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans = ""
        for i in range(0,len(A)):
            if(A[i] in "aeiouAEIOU"):
                ans = ans + A[i]
        return ans
