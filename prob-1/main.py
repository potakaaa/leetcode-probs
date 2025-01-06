class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):            
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]

        return None

test = Solution()

print(test.twoSum([3, 2, 4], 6)) # [0, 1]