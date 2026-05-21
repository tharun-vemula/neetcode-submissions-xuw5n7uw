class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            products.append(self.calculate_product(i, nums))
        return products
        
    def calculate_product(self, i: int, nums: List[int]) -> int:
        product = 1
        for j in range(len(nums)):
            if i != j:
                product = product * nums[j]
        return product