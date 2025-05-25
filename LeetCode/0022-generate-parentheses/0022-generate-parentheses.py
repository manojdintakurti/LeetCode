class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def backTracking(openP, closedP):
            if openP == closedP == n:
                res.append("".join(stack))
                return
            if openP < n:
                stack.append("(")
                backTracking(openP+1,closedP)
                stack.pop()
            if closedP<openP:
                stack.append(")")
                backTracking(openP,closedP+1)
                stack.pop()
        backTracking(0,0)
        return res
            