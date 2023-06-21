#User function Template for python3

class Solution:
	def is_palindrome(self, n):
	    n = str(n)
		i = 0
		j = len(n)-1
		while i<=j:
		    if n[i] != n[j]:
		        return ("No")
		    i+=1
		    j-=1
		return ("Yes")
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends