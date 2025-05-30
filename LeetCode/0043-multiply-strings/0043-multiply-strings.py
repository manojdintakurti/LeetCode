class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strToInt(s):
            num = 0
            for i in range(len(s)):
                num += (ord(s[i])-ord('0'))*(10**(len(s)-1-i))
                print(num)
            return num
        num1=strToInt(num1)
        num2=strToInt(num2)
        return str(num1*num2)