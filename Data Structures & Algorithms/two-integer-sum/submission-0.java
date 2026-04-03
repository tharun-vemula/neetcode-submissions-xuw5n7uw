class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> pairToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int remaining = target - nums[i];
            if (pairToIndex.containsKey(remaining)) {
                return new int[]{pairToIndex.get(remaining), i};
            }
            pairToIndex.put(nums[i], i);
        }
        return new int[]{};
    }
}
