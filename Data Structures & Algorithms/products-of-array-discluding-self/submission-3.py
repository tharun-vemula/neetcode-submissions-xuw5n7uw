class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = []
        left_product = 1
        right_products = [0] * len(nums)
        right_product = 1

        for i in range(len(nums)):
            left_products.append(left_product)
            left_product = left_product * nums[i]
            right_products[len(nums)-i-1] = right_product
            right_product = right_product * nums[len(nums)-i-1]            
        
        output = [0] * len(nums)

        for i in range(len(nums)):
            output[i] = left_products[i] * right_products[i]
        
        return output
        
            

           

    