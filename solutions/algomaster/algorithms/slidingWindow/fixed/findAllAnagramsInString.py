class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount, pCount = {}, {}
        sLen, pLen = len(s), len(p)

        if pLen > sLen:
            return []
        
        for i in range(pLen):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)

        result = [0] if sCount == pCount else []
        l = 0

        for r in range(pLen, sLen):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1

            if sCount == pCount:
                result.append(l)

        return result

    """
    FIXED SLIDING WINDOW
        Initialize frequency maps for p and sliding window of s
        Get lengths for simpler code

        Initialze the sliding window
        Iterate through len(p):
            Add characters to the map
        
        Initialize result variable based on if initial sliding window is equal to pCounts

        take left and right pointer
        left = 0, starting from begin
        right = len(p), starting from end of window

        Iterate from len(p) to len(s)
            Add right to sliding window, subtract left from
            If window[s[left]] is now 0, pop it from the map to make comparison in next step

            Increment L

            if sliding window and pCount are equal:
                append the left index to result array

        return restul array
    """
