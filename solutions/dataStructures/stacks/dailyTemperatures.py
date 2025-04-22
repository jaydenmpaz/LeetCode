class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)  # Store number of days until next warmer day

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)
        
        return res

        """
        While stack is not empty and the temperature of the current day is greater than the previous, 
            pop index from the stack and and subtract current index - popped
            append the index
        """
