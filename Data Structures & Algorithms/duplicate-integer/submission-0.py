class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        new = set(nums)
        return (len(new) != len(nums))