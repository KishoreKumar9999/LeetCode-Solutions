#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        a = N
        ans = 0
        while a!=0:
            d = a%10
            if d != 0:
                if N%d == 0:
                    ans += 1
            a = a//10
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends