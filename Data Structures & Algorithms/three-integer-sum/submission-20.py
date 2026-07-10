class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        tmp = []
        nums = sorted(nums)
        for i in range(n):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if (nums[l] + nums[r] + nums[i] == 0) and [nums[l], nums[r], nums[i]] not in tmp:
                        tmp.append([nums[l], nums[r], nums[i]])
                        r -= 1
                        l += 1
                    elif nums[l] + nums[r] + nums[i] < 0:
                        l += 1
                    else:
                        r -= 1
        return tmp