class Solution:
    def generate(self, numRows):
        l = [[1], [1, 1]]
        m = [[1]]
        n = [[1], [1,1]]
        i = 1
        a = [1]
        if numRows == 1:
            return(m)
        if numRows == 2:
            return(n)
        if numRows > 2 and numRows <= 30:
            for i in range(numRows-2):
                for j in range(0, len(l[-1])-1):
                    
                    x = l[-1][j] + l[-1][j+1]
                    a.append(x)
                a.append(1)
                l.append(a)
                a = [1]
                i = i+1
            return(l)
n = Solution()
n.generate(2)