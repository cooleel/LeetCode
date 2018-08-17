'''
7.Reverse Integer

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.

'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x > 0:
            res = int(str(x)[::-1])
            if -2**31 <= res <= 2**31 - 1:
                return res
            else:
                return 0
        else:
            res = -int(str(-x)[::-1])
            if -2**31 <= res <= 2**31 - 1:
                return res
            else:
                return 0
