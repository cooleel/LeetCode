'''
4.Median of Two Sorted Arrays

'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newList = nums1 + nums2
        newList = sorted(newList)

        if len(newList) %2 ==0:
            first = newList[len(newList)//2 -1]
            second = newList[len(newList)//2]
            me = (first+second)/2
            return me
        else:
            me = newList[len(newList)//2]
            return me
