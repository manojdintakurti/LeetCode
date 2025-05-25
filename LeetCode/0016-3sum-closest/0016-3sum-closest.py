from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 0
        minDiff = float('inf')

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                diff = abs(target - threeSum)

                if diff < minDiff:
                    minDiff = diff
                    closest = threeSum

                if threeSum < target:
                    l += 1
                else:
                    r -= 1

        return closest
