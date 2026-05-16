class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setVals = set(nums)
        if len(setVals) != len(nums):
            return True
        else:
            return False
        