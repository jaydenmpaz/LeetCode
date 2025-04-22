class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while (left != right):
            cur = numbers[left] + numbers[right]
            if (target > cur):
                left += 1
            elif (target < cur):
                right -= 1
            elif (target == cur):
                return [left + 1, right + 1]
        
    """
    INTUITION
        Initialize left and right pointers that converge to middle

        while left != right
            calculate the sum of the numbers at left and right
            if sum less than
                increment left
            elif sum greater than
                decrement right
            elif we found our sum
                return the result indexed correctly
    """