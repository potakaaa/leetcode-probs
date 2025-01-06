class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subset = []
        subset.append([])
        subset.append(nums)

        for i in range(len(nums)):
            extend = i
            for k in range(len(nums)):
                if nums[k:extend] not in subset:
                    subset.append(nums[k:extend])
                extend += 1

        return subset
    
arr = [1, 2, 3]

s = Solution()
print(s.subsets(arr))
        