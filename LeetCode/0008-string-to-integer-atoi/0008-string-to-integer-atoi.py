class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        res = 0
        for char in s:
            if not char.isdigit():
                break
            res = res * 10 + int(char)
            if sign == 1 and res >= 2**31 - 1:
                return 2**31 - 1
            if sign == -1 and res >= 2**31:
                return -2**31

        return sign * res
