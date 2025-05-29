class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
            return bound

        start = find_bound(True)
        end = find_bound(False)
        return [start, end]
