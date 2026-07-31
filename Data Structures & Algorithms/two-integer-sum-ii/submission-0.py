class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        first = 0
        last = len(numbers) - 1
        while first < last:
            if (numbers[first] + numbers[last] == target):
                result.append(first+1)
                result.append(last+1)
                return result
            if (numbers[first] + numbers[last] > target):
                last = last - 1
            else:
                first = first + 1
        return result

 
