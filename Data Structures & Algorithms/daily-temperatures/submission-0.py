class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            for j in range(i, n):
                if temperatures[i] < temperatures[j]:
                    diff = j - i
                    result[i] = diff
                    break
        return result
            