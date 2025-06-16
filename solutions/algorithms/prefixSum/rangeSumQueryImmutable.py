class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        for i in range(len(nums) - 1):
            self.array[i + 1] += self.array[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.array[right] if left == 0 else self.array[right] - self.array[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

"""
INTUITION CALCULATE PRESUM AND THEN USE LEFT AND RIGHT INDICES AS BOUNDS

    def __init__(self, nums: List[int]):
        Pass in as a pointer
        calculate the presum by looping through and setting the values of [i + 1] += i
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return right index of presum array
        else:
            return the difference of the presum calculated at right and left - 1
"""