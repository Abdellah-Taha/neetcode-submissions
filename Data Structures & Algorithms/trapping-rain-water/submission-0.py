class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = 0, 0
        
        total_water = 0
        for i in range(len(height)):
            max_r = max(height[i:])
            if max_l < height[i]:
                max_l = height[i]
            value = min(max_l, max_r) - height[i]
            if value > 0:
                total_water += value
        return total_water

