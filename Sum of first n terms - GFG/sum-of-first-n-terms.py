#User function Template for python3

class Solution:
    def sumOfSeries(self,N):
        sum = ((N*(N+1))//2)**2
        return int(sum)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
# } Driver Code Ends