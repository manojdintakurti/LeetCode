class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        """
        left, right = 0, len(height)-1
        max_area = 0
        while left<right:
            width = right - left
            heigh = min(height[right],height[left])
            max_area = max(width*heigh,max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_area
