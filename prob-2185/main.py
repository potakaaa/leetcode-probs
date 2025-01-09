class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for word in words:
            count += 1 if word.startswith(pref) else None
        return count

test = Solution()

print(test.prefixCount(["abab","ab"], "ab")) # 2