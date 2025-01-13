class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {}
        for i in range(len(s)):
            if s[i] in dicts:
                dicts[s[i]] += 1
            else:
                dicts[s[i]] = 1

        length = 0
        for k, v in dicts.items():
            while (v > 2):
                dicts[k] -= 2
                v -= 2
            length += v
    
        return length
        

test = Solution()
s = "abaacbcbb"
print(test.minimumLength(s))