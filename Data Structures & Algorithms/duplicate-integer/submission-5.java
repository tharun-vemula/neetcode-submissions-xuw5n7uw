class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numsInSet = new HashSet<>((int)((nums.length/0.75f) + 1));
        for(int num: nums) {
            if(!numsInSet.add(num)){
                return true;
            }
        }
        return false;
    }
}