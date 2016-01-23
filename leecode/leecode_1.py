class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums <= 1:
		    return False
			
        for i in range(len(nums)):
            for j in range(len(nums))[i+1:]:
                if nums[i] + nums[j] == target:
                    r = [i+1,j+1]
        return r
       


nums = [31,12,4,6]
b = 10
c = Solution()

print c.twoSum(nums,b)


"""
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i+1]
            else:
                buff_dict[target - nums[i]] = i+1
"""


