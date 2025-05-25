class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev = 0
        x = abs(x)
        while x != 0:
            pop = x % 10
            x //= 10

            if rev > (2**31 - 1)//10 or (rev == (2**31 - 1) //10 and pop > 7):
                return 0
            rev = rev*10 + pop
        return rev * sign

