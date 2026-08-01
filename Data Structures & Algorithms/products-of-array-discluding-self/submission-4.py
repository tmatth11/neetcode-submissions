class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prefix = 1

        for i in range(n):
            res.append(prefix)
            prefix *= nums[i]

        suffix = 1

        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res