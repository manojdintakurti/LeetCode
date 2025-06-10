class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0 : return False
        if n == 1: return True
        p={2,3,5}
        for i in p:
            while n%i == 0:
                n//=i
        return True if n == 1 else False
