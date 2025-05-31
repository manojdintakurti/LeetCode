class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        starIdx = -1
        match = 0

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                starIdx = j
                match = i
                j += 1
            elif starIdx != -1:
                j = starIdx + 1
                match += 1
                i = match
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)

            
