'''
169Majority Element

'''


from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       # major = []
        dic = Counter(nums)
        for key in dic:
            if dic[key] >= len(nums)/2:
                return key
                #major.append(key)
          #return major
