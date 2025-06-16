class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opens, closed, s):
            if opens == closed and opens + closed == n * 2:
                res.append(s)
                return
            
            if opens < n:
                dfs(opens + 1, closed, s + "(")
            if closed < opens:
                dfs(opens, closed + 1, s + ")")
            
        dfs(0, 0, "")

        return res


    """
    Initialize result array
    Define dfs function, open counter, closed counter, current as parameters
    If number of open + closed are equal and total length is n * 2, we have a valid combination
        Append the result

    if opens < n, we can add another open parent
        recursively call with open incremented and add "("
    
    if closed < open, we can balance by adding a closed 
        recursively call with closed incremented and add ")"

    initial call with dfs(0, 0, "")

    return result array
    """