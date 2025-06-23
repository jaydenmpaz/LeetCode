class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []

        for i in range(0, len(s), k):
            group = s[i : i+k]
            if len(group) < k:
                group += fill * (k - len(group))
            ans.append(group)

        return ans


        # n = len(s)
        # ans = []
        # full_groups = n // k
        # extra = n % k
        # print(extra)

        # for x in range(full_groups):
        #     start = k * x
        #     end = start + k
        #     curr = s[start : end]
        #     ans.append(curr)

        # if extra > 0:
        #     start = k * (full_groups)
        #     curr = s[start:]
        #     curr += fill * (k - extra)
        #     ans.append(curr)

        # return ans
        

    # Repeat the question:
    # Given a string s that can be partitioned into groups of size k where
    # - The first group is first k characters, second is second k characters, and so on
    # - The last group does not have to have k characters, which we can fill the remaining slots with the value fill

    # The partition is done in a way such that removing any fill characters from the last group
    # and joining the groups in order results in s.

    # Given s, k (size of groups), and fill, return a string array that contains
    # the composition of every k sized group in s.

    # Clarifying questions:
    # - If there are exactly enough letters to where we do not need to fill,
    #   just return the result as is?
    # - Are there any constraints on our input>
    # - Are there any operations we are not allowed to use?


    # Use Examples:
    # Input: s = "abc", k = 1, fill = "x"
    # Expected: ["a", "b", "c"]

    # Input: s = "abc", k = 5, fill = "x"
    # Expected: ["abcxx"]

    # Input: s = "abc", k = 3, fill = "x"
    # Expected: ["abc"]

    # Brainstorm Solution:
    # Index jumping
    # Simply use a for loop to jump k steps and get each group
    # IF at the last group, which can be denoted by len(group) < k
    # Fill it with the corresponding amount of fill values
    # Append to res array
    # Return after iteration

    # String slicing
    # Get the total length of the string, with this we can get
    # - The number of whole groups of k we can make
    # - Find out how much fill characters the last group will need, if any
    # Then, use string slicing to get groups then add to array, and special case for the last

    # Brute force
    # Use for loops to pass through every index, brute force and counting to extract the groups,
    # then append to array.