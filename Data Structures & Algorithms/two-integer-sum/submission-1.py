class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_idx = {}
        for idx, val in enumerate(nums):
            difference = target - val
            if difference in seen_idx:
                return [seen_idx[difference], idx]
            else:
                seen_idx[val] = idx
        