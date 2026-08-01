class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights) - 1
        area = 0
        while first<last:
            if heights[first] > heights[last]:
                if (heights[last] * (last - first)) > area:
                    area = heights[last] * (last - first)
                last = last - 1
            else:
                if (heights[first] * (last - first)) > area:
                    area = heights[first] * (last - first)
                first = first + 1
        return area
 