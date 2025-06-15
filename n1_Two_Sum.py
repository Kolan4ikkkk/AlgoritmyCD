class Solution(object):
    def twoSum(self, nums, target):
      
        num_map = {}  # створимо словник для зберігання вже пройдених чисел
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i