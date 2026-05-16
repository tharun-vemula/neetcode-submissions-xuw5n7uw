class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] ans = new int[k];
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num: nums) {
            counter.put(num, 1 + counter.getOrDefault(num, 0));
        }

        List<int[]> arr = new ArrayList<>();

        for(Map.Entry<Integer, Integer> entry: counter.entrySet()) {
            arr.add(new int[]{entry.getValue(), entry.getKey()});
        }
        arr.sort((a,b) -> b[0] - a[0]);
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = arr.get(i)[1];
        }
        return res;
        
    }
}
