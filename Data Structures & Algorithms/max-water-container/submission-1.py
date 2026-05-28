class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        storage = 0
        
        while left < right:
            small = min(heights[left], heights[right])
            curr = small * (right - left)
            storage = max(storage, curr)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1

        return storage
        