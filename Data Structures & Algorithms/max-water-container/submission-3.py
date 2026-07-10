class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        surface = 0
        i = 0
        while i < n:
            if min(heights[i], heights[n - 1]) * (n - 1 - i) > surface:
                surface = min(heights[i], heights[n - 1]) * (n - 1 - i)
            if heights[i] > heights[n - 1]:
                n -= 1
            else:
                i += 1
        return surface