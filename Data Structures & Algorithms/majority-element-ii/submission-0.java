class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int requiredOccurences = nums.length / 3;
        List<Integer> ans = new ArrayList<>();

        Map<Integer, Integer> counter = new HashMap<>((int)((nums.length / 0.75)+1));
        for (int num: nums) {
            counter.put(num, counter.getOrDefault(num, 0) +1);
        }

        for(int num: counter.keySet()) {
            int frequency = counter.get(num);
            if ( frequency > requiredOccurences ) {
                ans.add(num);
            }
        }
        return ans;
    }
}