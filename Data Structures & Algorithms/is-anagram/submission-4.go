func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    var charCounts [26]int

    for i := 0; i < len(s); i++ {
        charCounts[s[i] - 'a']++
        charCounts[t[i] - 'a']--
    }

    for _, count := range charCounts {
        if count != 0 {
            return false
        }
    }
    return true
}
