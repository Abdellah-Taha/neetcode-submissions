class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s: dict = {}
        for i in nums:
            s.setdefault(i, nums.count(i))
        res = sorted(s, key=lambda x:s[x], reverse=True)
        return res[:k]