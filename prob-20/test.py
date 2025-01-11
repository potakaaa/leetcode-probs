class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if stack and stack[-1] == "(" and s[i] == ")":
                stack.pop()
            elif stack and stack[-1] == "[" and s[i] == "]":
                stack.pop()
            elif stack and stack[-1] == "{" and s[i] == "}":
                stack.pop()
            else:
                stack.append(s[i])            
        
        return True if not stack else False
 
s = "()[]{}"
test = Solution()
print(test.isValid(s)) # True
