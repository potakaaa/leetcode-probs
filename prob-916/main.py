class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """

        max_freq = {}

        for word in words2:
            for letter in word:
                if letter in max_freq:
                    max_freq[letter] = max(max_freq[letter], word.count(letter))
                else:
                    max_freq[letter] = word.count(letter)

        res = []
        for word in words1:
            temp = 0
            if all([word.count(letter) >= freq for letter, freq in max_freq.items()]):
                res.append(word)
        
        return res

            

            
        


words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

test = Solution()
print(test.wordSubsets(words1, words2)) # ["facebook","google","leetcode"]