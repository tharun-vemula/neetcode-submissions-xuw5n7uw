class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            sorted_str = str(sorted(string))
            if sorted_str in result:
                result[sorted_str].append(string)
            else:
                result[sorted_str] = [string]
        
        return list(result.values())