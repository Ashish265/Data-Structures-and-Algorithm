class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d= {}
        
        for i,n in enumerate(nums):
            if n in d:
            	return[d[n],i]
            d[target-n]=i


s= Solution()

print(s.twoSum([5,4,7,6,8,6],9))