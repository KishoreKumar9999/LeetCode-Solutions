class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        heapq.heapify(stones)
        while len(stones)>=2:
            y = heapq.heappop(stones)
            print(stones)
            x = heapq.heappop(stones)
            print(stones)
            heapq.heappush(stones, y-x)
            print(stones)
        return -1*stones[0]
        