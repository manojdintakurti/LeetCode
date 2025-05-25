class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        maps={')':'(','}':'{',']':'['}
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack)==0 or maps[i]!=stack[-1]:
                    return False
                else:
                    stack.pop()
        return True if len(stack)==0 else False