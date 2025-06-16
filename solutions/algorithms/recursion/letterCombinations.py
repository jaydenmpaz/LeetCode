class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []

        mapping = {"2": "abc", "3": "def", "4": "ghi", 
        "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def helper(digits, string):
            if not digits:
                res.append(string)
                return
                
            letters = list(mapping.get(digits[0]))

            for letter in letters:
                helper(digits[1:], string + letter)

        helper(digits, "")
        return res