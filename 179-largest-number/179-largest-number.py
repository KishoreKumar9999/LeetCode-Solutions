class LargestNumberKey(str):
    def __lt__(x, y) -> bool:
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = ''.join(sorted(map(str, nums), key=LargestNumberKey))
        return "0" if largest[0] == "0" else largest
        
        