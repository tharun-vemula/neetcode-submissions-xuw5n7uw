class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        Arrays.sort(nums);
        int maxLength = 1;
        int currentLength = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            int difference = nums[i+1] - nums[i];
            if (difference == 1) {
                currentLength += 1;
            } 
            else if (difference == 0 ) {
                continue;
            } 
            else {
                maxLength = Math.max(currentLength, maxLength);
                currentLength = 1;
            }
        }
        maxLength = Math.max(currentLength, maxLength);
        return maxLength;
    }
}
