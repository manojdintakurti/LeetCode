class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxSoFar=""
        flag=0
        for i in range(len(strs[0])):
            for j in strs:
                if i==len(j) or strs[0][i]!=j[i]:
                    flag=1
                    break
            if flag==1:
                break
            maxSoFar+=strs[0][i]
        return maxSoFar

                