class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, e in enumerate(nums):
            diff = target - e
            if diff in num_map:
                return [num_map[diff], i]
            
            num_map[e] = i