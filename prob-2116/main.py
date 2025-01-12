class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        
        if len(s) % 2 == 1:
            return False
            
        unlocked_stack = []
        locked_stack = []
        
        for i in range(len(s)):
            if locked[i] == "0":
                unlocked_stack.append(i)
            elif s[i] == "(":
                locked_stack.append(i)
            else:
                if locked_stack:
                    locked_stack.pop()
                elif unlocked_stack:
                    unlocked_stack.pop()
                else:
                    return False

        while locked_stack and unlocked_stack and locked_stack[-1] < unlocked_stack[-1]:
                locked_stack.pop()
                unlocked_stack.pop()
        
        if locked_stack:
            return False

        return True

        
    

s = "()"
locked = "11"
test = Solution()
print(test.canBeValid(s, locked)) # True

