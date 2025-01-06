class Solution(object):
    def twoSum(self, nums, target):
        dicts = {}
        ans = []
        for i in range(len(nums)):
            if (target - nums[i]) in dicts:
                ans.append(dicts[target - nums[i]])
                ans.append(i)
            else:
                dicts[nums[i]] = i
        return ans

test = Solution()

print(test.twoSum([2, 1, 6, 8], 9)) # [0, 1]