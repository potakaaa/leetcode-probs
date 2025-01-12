class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        
        if (s[0] == ")" and locked[0] == "1") or len(s) % 2 != 0:
            return False
        
        unlocked_stack = []
        locked_stack = []
        for i in range(len(s)):
            if locked == "0" and s[i] == "(":
                unlocked_stack.append(i)
            elif locked == "0" and s[i] == ")":
                if locked_stack:
                    locked_stack.pop()
                elif unlocked_stack:
                    unlocked_stack.pop()
            elif locked == "1" and (s[i] == "(" or s[i] == ")"):
                locked_stack.append(i)

        while locked_stack and unlocked_stack and locked_stack[-1] < unlocked_stack[-1]:
                locked_stack.pop()
                unlocked_stack.pop()
        
        if locked_stack:
            return False

        return True

        
    

s = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
locked = "100011110110011011010111100111011101111110000101001101001111"
test = Solution()
print(test.canBeValid(s, locked)) # False