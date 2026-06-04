class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        p= ""

        for i in range(len(strs[0])):
            c = strs[0][i]
            for word in strs[1:]:
                if i >= len(word):
                    return p

                if word[i] != c:
                    return p

            p += c

        return p