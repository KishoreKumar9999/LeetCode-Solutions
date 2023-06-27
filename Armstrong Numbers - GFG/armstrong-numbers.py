#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        a = n
        sum = 0
        while n>0:
            d = n%10
            c = d**3
            sum += c
            n = n//10
        if sum == a:
            return("Yes")
        else:
            return("No")


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends