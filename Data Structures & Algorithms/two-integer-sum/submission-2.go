func twoSum(nums []int, target int) []int {
    pairToIndex := make(map[int]int)
    for idx, val := range nums {
        diff := target - val
        if seen_idx, ok := pairToIndex[diff]; ok {
            return []int{seen_idx, idx}
        }
        pairToIndex[val] = idx
    }
    return []int{}
}
