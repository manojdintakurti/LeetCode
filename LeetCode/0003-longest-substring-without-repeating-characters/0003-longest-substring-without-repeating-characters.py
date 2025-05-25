class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLen=0
        chars=[]
        for i in range(len(s)):
            if (s[i] not in chars):
                chars.append(s[i])
            else:
                index=chars.index(s[i])
                chars=chars[index+1:]
                chars.append(s[i])
            if(len(chars)>maxLen):
                maxLen=len(chars)
        return maxLen

