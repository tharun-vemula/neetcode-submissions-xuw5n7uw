class Solution:
    def maxArea(self, heights: List[int]) -> int:
        storage = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                small = min(heights[i], heights[j])
                curr = small * (j - i)
                storage = max(storage, curr)
        return storage
        