class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strToInt(s):
            num = 0
            for i in range(len(s)):
                num =num*10+ (ord(s[i])-ord('0'))
            return num
        num1=strToInt(num1)
        num2=strToInt(num2)
        return str(num1*num2)