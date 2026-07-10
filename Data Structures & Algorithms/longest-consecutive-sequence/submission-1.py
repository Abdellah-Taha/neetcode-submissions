class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = 1
        tmp = []
        nums = sorted(set(nums))
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] != 1:
                tmp.append(n)
                n = 0
            n += 1
        tmp.append(n)
        print(nums)
        return max(tmp)
