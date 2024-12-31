class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subset = []
        subset.append([])
        subset.append(nums)

        k, j = 0, 0

        while (k < len(nums)):
            temp = []
            while (temp.extend([nums[j]]) not in subset):
                temp.append(nums[k])
                subset.append(temp.extend([nums[j]]))
                j += 1
            k += 1

        return subset
    
arr = [1, 2, 3]

s = Solution()
print(s.subsets(arr))
        