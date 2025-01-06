class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        _1 = []
        ans = [0] * len(boxes)
        for i in range(len(boxes)):
            if boxes[i] == '1':
                _1.append(i)
            
            for j in range(i + 1, len(boxes)):
                if boxes[j] == '1':
                    ans[i] += abs(i - j)
            ans[i] += sum([abs(i - x) for x in _1])
        return ans
        
    
test = Solution()

print(test.minOperations("110")) # [1, 1, 3]