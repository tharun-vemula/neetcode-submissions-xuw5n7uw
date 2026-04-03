class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        int prefixProduct = 1;
        int suffixProduct = 1;

        for (int i = 0; i < nums.length; i++) {
            prefix[i] = prefixProduct;
            prefixProduct = nums[i] * prefixProduct;
        }

        for (int i = nums.length-1; i >= 0; i--) {
            suffix[i] = suffixProduct;
            suffixProduct = nums[i] * suffixProduct;
        }

        for (int i = 0; i < nums.length; i++) {
            output[i] = prefix[i] * suffix[i];
        }

        return output;
    }
}  
