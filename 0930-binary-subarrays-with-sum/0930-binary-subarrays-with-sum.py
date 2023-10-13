class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = {0: 1}  # Initialize a dictionary to store prefix sums and their counts.
        current_sum = 0  # Initialize the current sum.
        count = 0  # Initialize the count of subarrays.

        for num in nums:
            current_sum += num  # Calculate the current sum.

            # Check if there is a prefix sum that, when subtracted from the current sum, equals the goal.
            if current_sum - goal in prefix_sum:
                count += prefix_sum[current_sum - goal]

            # Update the prefix sum dictionary.
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1

        return count
