class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        freq = {}
        total = 0
        res = []

        for i in range(len(A)):
            if A[i] not in freq:
                freq[A[i]] = 1
            elif A[i] in freq:
                freq[A[i]] += 1
                total += 1
            if B[i] not in freq:
                freq[B[i]] = 1
            elif B[i] in freq:
                freq[B[i]] += 1
                total += 1

            res.append(total)
            
        return res
            
             
        
    
test = Solution()
A = [1,3,2,4]
B = [3,1,2,4]
print(test.findThePrefixCommonArray(A, B))