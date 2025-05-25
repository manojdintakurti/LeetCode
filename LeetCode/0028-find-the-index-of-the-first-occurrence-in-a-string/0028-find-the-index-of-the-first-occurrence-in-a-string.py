class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenNeedle=len(needle)
        lenHaystack=len(haystack)
        for i in range(len(haystack)):
            if(haystack[i]==needle[0]):
                if(lenNeedle==1 or lenHaystack==1):
                    return i
                if(i+lenNeedle<=lenHaystack):
                    if(haystack[i:i+lenNeedle]==needle):
                        return i
        return -1