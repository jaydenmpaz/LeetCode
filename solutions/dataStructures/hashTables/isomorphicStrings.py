class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_ind = {}
        t_ind = {}

        for i in range(len(s)):
            if s[i] not in s_ind:
                s_ind[s[i]] = i
            if t[i] not in t_ind:
                t_ind[t[i]] = i
            if s_ind[s[i]] != t_ind[t[i]]:
                return False
        
        return True
    
    """
    INTUITION 

    For both strings s and t, create a hashtable to map each character to an index

        Initialize s indexes and t indexes hash tables

        for i in range(len(s)):
            if current character in s not in hashtable:
                add it to map with value of index
            if current character in t not in hashtable:
                add it to map with value of index

            if the char in s and char in t are mapped to different indices:
                return False
        
        reutrn True
    """

    """
    Alternatively, we can also use one hash table, and map the instance in s to t and check for repeating/incorrect mappings
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        for sc, tc in zip(s, t):
            if sc in mapping:
                if mapping[sc] != tc:
                    return False
            elif tc in mapping.values():
                return False
            
            mapping[sc] = tc
        
        return True
    """