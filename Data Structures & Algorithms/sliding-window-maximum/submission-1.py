class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        
        i = 0
        j = k-1
        result = []
        while j<len(nums):
            max_value = max(nums[i:j+1])
            result.append(max_value)
            i += 1
            j += 1

        return result  
        