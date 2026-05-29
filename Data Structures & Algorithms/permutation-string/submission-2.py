class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        left = 0
        right = len(s1)

        while right <= len(s2):
            s = s2[left: right]
            if self.issubstring(s1, s):
                return True
            else:
                left += 1
                right += 1
        return False
    
    def issubstring(self, s1: str, s2: str):
        return sorted(s1) == sorted(s2)
        