class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)

        return list(res.values())


    """
    INTUITION
        Create a default dictionary which takes list as values
        for string in strings
            we want to generate a common anagram, so sort the string
            then append the string with the common key to dictioinary 

        return a list of all the values in our dcitionary, which should be a list of lists
    """
