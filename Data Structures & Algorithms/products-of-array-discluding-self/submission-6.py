class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left_products = [0] * size
        left_product = 1
        right_products = [0] * size
        right_product = 1

        for i in range(size):
            left_products[i] = left_product
            left_product = left_product * nums[i]
            right_products[size-i-1] = right_product
            right_product = right_product * nums[size-i-1]            
        
        output = [0] * size

        for i in range(size):
            output[i] = left_products[i] * right_products[i]
        
        return output
        
            

           

    