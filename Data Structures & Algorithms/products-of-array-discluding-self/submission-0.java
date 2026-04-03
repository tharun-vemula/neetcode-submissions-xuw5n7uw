class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        for (int j = 0; j < nums.length; j++) {
            int product = getProduct(j, nums);
            output[j] = product;
        }
        return output;
    }

    public int getProduct(int idx, int[] nums) {
        int product = 1;
        for (int i = 0; i < nums.length; i++) {
            if ( i == idx) {
                continue;
            }
            product = product * nums[i];
        }
        return product;
    }
}  
