class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        tmp = []
        nums = sorted(nums)
        for i in range(n):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0 and [nums[i], nums[l], nums[r]] not in tmp:
                    tmp.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return tmp