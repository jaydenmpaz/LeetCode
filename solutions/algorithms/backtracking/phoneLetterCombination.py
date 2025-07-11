class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(path, idx):
            if idx == len(digits):
                result.append(path)
                return

            for letter in phone[digits[idx]]:
                backtrack(path + letter, idx + 1)

        if digits:
            backtrack("", 0)

        return result