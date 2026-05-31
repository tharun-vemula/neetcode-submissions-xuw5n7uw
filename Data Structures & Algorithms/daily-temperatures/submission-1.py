class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = idx - index
            stack.append((temperature, idx))
        
        return result
            
            