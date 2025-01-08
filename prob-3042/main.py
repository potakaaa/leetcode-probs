class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        ans = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        
        return ans

    def isPrefixAndSuffix(self, str1, str2):
        return str1.startswith(str2) and str1.endswith(str2)
        


test = Solution()
str1 = ["abab","ab"]

#print(test.countPrefixSuffixPairs(str1)) # 4

print(test.isPrefixAndSuffix("abab", "ab")) # False