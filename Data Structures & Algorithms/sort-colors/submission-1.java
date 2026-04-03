class Solution {
    public void sortColors(int[] nums) {
       int left = 0, i = 0;
    int right = nums.length - 1;

    while (i <= right) {
        if (nums[i] == 0) {
            swap(nums, left, i);
            left++;
            i++; 
        } else if (nums[i] == 2) {
            swap(nums, right, i);
            right--;
        } else {
            i++; 
        }
    }
    }

    private void swap(int arr[], int low, int high) {
        int ans = arr[low];
        arr[low] = arr[high];
        arr[high] = ans;
    }
}