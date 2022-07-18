# from queue import PriorityQueue
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         res = []
#         ret = []
#         res = PriorityQueue()
#         for i in range(len(points)):
#             ans1 = (points[i][0]*points[i][0]) 
#             ans2 = (points[i][1]*points[i][1])
#             ans = ans2+ans1
#             res.put([ans,points[i]])
#         for i in range(k):
#             ret.append(res.get()[1])
#         return ret
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])
        
        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res
        