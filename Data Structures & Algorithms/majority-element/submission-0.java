class Solution {
    public int majorityElement(int[] nums) {
        int size = nums.length;
        HashMap<Integer, Long> counter = new HashMap<>((int)(size / 0.75f) + 1);
        for (int num: nums) {
            counter.merge(num, 1L, Long::sum);
        }
        int requiredSize = size / 2;
        int k = 0;
        for (Map.Entry<Integer, Long> entry : counter.entrySet()) {
            int key = entry.getKey();
            Long value = entry.getValue();
            if (value > requiredSize) {
                return key;
            }
        }
        return k;
    }
}