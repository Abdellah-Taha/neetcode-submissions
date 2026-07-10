
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * (len(nums) + 1)
        s = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            p[i+1] = p[i] * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            s[i] = s[i+1] * nums[i] 
        return [p[i] * s[i + 1] for i in range(len(nums))]
