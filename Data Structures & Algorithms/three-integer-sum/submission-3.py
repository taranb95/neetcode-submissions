class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        result = []

        for idx,num in enumerate(nums):
            hashmap[num] = idx
        
        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                num_find = 0 - (nums[first] + nums[second])
                if num_find in hashmap and hashmap[num_find] > second:
                    res = sorted([nums[first], nums[second], num_find])
                    if res not in result:
                        result.append(res)
        return result