func isAnagram(s string, t string) bool {
    sfreq := make(map[rune]int)
    tfreq := make(map[rune]int)
    for _, char := range s {
        val := sfreq[char]
        sfreq[char] = val + 1
    }

    for _, char := range t {
        val := tfreq[char]
        tfreq[char] = val + 1
    }

    for char, val := range sfreq {
        val2 := tfreq[char]
        if val2 != val {
            return false
        }
    }

    for char, val := range tfreq {
        val2 := sfreq[char]
        if val2 != val {
            return false
        }
    }
    return true
}
