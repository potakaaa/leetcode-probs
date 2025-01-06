class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ans = []
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes) - i - 1):
               if boxes[j] == "1":
                    ans.append(j-i)
        return ans 
    
test = Solution()

print(test.minOperations("110")) # [1, 1, 3]