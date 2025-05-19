class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0

        while i < j:
            length = j - i
            cheight = min(height[i], height[j])
            current = length * cheight

            res = max(res, current)

            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        
        return res

    """
    INTUITION 2 POINTER
        i = 0
        j = len(height) - 1
        initialize res = 0

        while i < j (converging):
            length = distance between j and i pointers
            calculate the minimum height between the 2
            calculate the current area

            check the max between result variable and current

            then increment or decrement based on the lower value, because shoter height is bottleneck
            Length shrinks as move closer, so we need to take larger height
        
        return res
    """