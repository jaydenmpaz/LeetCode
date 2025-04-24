class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = collections.Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count

    # Intuition:
    # Group numbers from 1 to n based on the sum of their digits.
    # For example, 13 → sum = 1 + 3 = 4, so 13 belongs to group "4".
    # Use a hashmap to count how many numbers fall into each digit-sum group.
    # Then, find the size of the largest group(s), and count how many groups have that size.