class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        freq = {}
        # Get frequency of each value
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        # Index: Frequency, Value: Numbers with that frequency in array
        buckets = [[] for i in range(len(nums) + 1)]
        
        # Add frequencies to buckets
        for key, value in freq.items():
            buckets[value].append(key)

        # Iterate through buckets backwards until k is reached
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                
                if len(res) == k:
                    return res