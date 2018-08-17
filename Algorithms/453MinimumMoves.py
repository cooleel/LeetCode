'''
453 Minimun Moves to Equal Array Elements
Given a non-empty integer array of size n,
find the minimum number of moves required to make all array elements equal,
where a move is incrementing n - 1 elements by 1.


hints:
afte x moves, all values in this array will be equal to x+min
total_value = N * (x+min)
total_value = sum(input) + x * (N-1)
therefore:

N * (x+min) = sum(input) + x *(N-1)
x = sum(input) - N*min

'''

def minMoves(nums):
    return sum(nums) - min(nums) * len(nums)
