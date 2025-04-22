class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        res = 0
        majority = 0

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > majority:
                res = num
                majority = counts[num]

        return res

    
    """
    Initialize dictionary to count frequencies
    Initialize result variable to return
    Initialize majority variable to compare frequencies

    for number in array:
        increment frequency of that number by one
        if the new frequency is higher than old
            set result to that number
            set majority to that number's freq
    
    return result
    """


    """
    O(1) solution
    Intuition is Every time current number is the same as res, we add +1 to majority. If not, we add -1 to majority.

    When majority is 0, it's time to change majority number(= res), 
    because every time current number and res are different, we add -1 to majority, 
    so if majority is 0, that means a current majority number(= res) is not the majority number anymore. 
    That's why when majority is 0, update res with current number.

    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0

        for n in nums:
            if majority == 0:
                res = n
            
            majority += 1 if n == res else -1
        
        return res
    """