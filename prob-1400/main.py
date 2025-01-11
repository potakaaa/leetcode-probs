'''
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
'''

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False

        if len(s) == k:
            return True
        
        freq = {}

        for letter in s:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        

        odd_count = 0
        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1

        return odd_count <= k
    
s = "annabelle"
test = Solution()
print(test.canConstruct(s, 2)) # True
        