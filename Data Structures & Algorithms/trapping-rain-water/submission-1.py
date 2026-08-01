class Solution:
    def trap(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        leftmax = height[first]
        rightmax = height[last]
        res = 0
        while first < last:
            if leftmax < rightmax:
                first += 1
                leftmax = max(leftmax,height[first])
                res += leftmax - height[first]
            else:
                last -= 1
                rightmax = max(rightmax,height[last])
                res += rightmax - height[last]
        return res

        