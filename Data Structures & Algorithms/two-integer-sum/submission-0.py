class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            for j, value in enumerate(nums):
                if (nums[i] + nums[j] == target) and i != j:
                    return [i,j]