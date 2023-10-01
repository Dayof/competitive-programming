# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

from typing import List


class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Runtime: 43ms, memory 16.41 MB.
        Time O(n), memory O(n).
        """
        result = []
        past_sum = 0
        for idx in range(len(nums)):
            result.append(nums[idx] + past_sum)
            past_sum += nums[idx]
        return result

class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Runtime: 37ms, memory 16.40 MB.
        Time O(n), memory O(n).
        """
        size = len(nums)
        if size == 0:
            return []

        result = [0] * size
        result[0] = nums[0]
        for idx in range(1, size):
            result[idx] = result[idx - 1] + nums[idx]
        return result

class Solution3:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Runtime: 49ms, memory 16.55 MB.
        Time O(n), memory O(1).
        """
        for idx in range(1, len(nums)):
            nums[idx] = nums[idx - 1] + nums[idx]
        return nums


class Solution4:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Runtime: 53ms, memory 16.46 MB.
        Time O(n^2), memory O(n).
        """
        return [sum(nums[:idx+1]) for idx in range(len(nums))]

# Doc:
# Our constraints would require up to 1MB (1000 elements) in theory if each element would
# require 1 bytes, but is it so, let's understand how lists are created.

# Here are some python code executions to showcase how many bytes empty lists takes
# and lists with elemtens:
 
# >>> sys.getsizeof([])
# 56
# >>> sys.getsizeof([1])
# 64
# >>> lst = []
# >>> lst.append(1)
# >>> sys.getsizeof(lst)
# 88
# >>> sys.getsizeof([1000000]*1000)
# 8056

# As we can see above, the maximum size for our constrains would be 8MB instead of 1MB.
# Each element consumes 8 bytes, which is the smallest block size in the Python heap object allocator.
# The heap block can allocate from 8 bytes to 512 bytes, but it needs to be a multiple of eight.

# Now let's discuss about the method 4, even though it looks quite
# efficient in terms of memory complexity, I would never use this
# in real life case since it overrides the input value.

# In python, dynamic types are passed as reference, not copy,
# so we need to be careful on how we manipulate our method arguments.   

# Python has a pymalloc allocator optimized for small objects 
# (smaller or equal to 512 bytes) with a short lifetime. 
# It uses memory mappings called “arenas” with a fixed size of 256 KiB. 
# It falls back to PyMem_RawMalloc() and PyMem_RawRealloc() for allocations 
# larger than 512 bytes (ref: https://docs.python.org/3.10/c-api/memory.html#the-pymalloc-allocator).