class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return n
        curr=1
        while curr<len(nums):
            if nums[curr-1]==nums[curr]:
                nums.pop(curr)
            else:
                curr+=1

            
        return len(nums)