class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for char in s:
            if char == ")" and "(" in stack:
                stack.remove("(")
            elif char == "]" and "[" in stack:
                stack.remove("[")
            elif char == "}" and "{" in stack:
                stack.remove("{")
            else:
                stack.append(char)
            
        
        return True if not stack else False
                
s = "([)]"
test = Solution()
print(test.isValid(s)) # True

st = ["]"]
print(st[-1])