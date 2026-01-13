# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of numbers.
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
        """Runtime: 0ms, memory 19.42 MB.
        Time O(n), memory O(n).
        Date: 12/01/2026
        """
        result = []
        past_sum = 0
        for idx in range(len(nums)):
            result.append(nums[idx] + past_sum)
            past_sum += nums[idx]
        return result


class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Runtime: 0ms, memory 19.6 MB.
        Time O(n), memory O(n).
        Date: 12/01/2026
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
        """Runtime: 0ms, memory 19.48 MB.
        Time O(n), memory O(1).
        Date: 12/01/2026
        """
        for idx in range(1, len(nums)):
            nums[idx] = nums[idx - 1] + nums[idx]
        return nums


class Solution4:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Runtime: 11ms, memory 19.59 MB.
        Time O(n^2), memory O(n).
        Date: 12/01/2026
        """
        return [sum(nums[: idx + 1]) for idx in range(len(nums))]


class Solution5:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Runtime: 11ms, memory 19.48 MB.
        Time O(n^2), memory O(n).
        Date: 12/01/2026
        """
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = sum(nums[0 : i + 1])
        return output


class Solution6:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Runtime: 0ms, memory 19.36 MB.
        Time O(n), memory O(1).
        Date: 12/01/2026
        Similar to Solution2.
        """
        input_size = len(nums)
        output = [0] * input_size
        running_sum = 0
        for i in range(input_size):
            running_sum += nums[i]
            output[i] = running_sum
        return output


## Memory details:

# memory: 1k values of int 32
# int 32 could go up to ~ 2.1 billion, so in terms of language constrainst this wouldn't
# be a problem to store 1k values of int 32, taking into account each int 32 takes 4
# bytes, we would have 4k bytes, which is approx 4 KiB and approx 0.0038 MiB.

# Let's understand how lists are created. Here are some python code executions to
# showcase how many bytes empty lists takes and lists with elemtens:

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

# As we can see above, the maximum size for our constrains would be 8 KiB.
# Each element consumes 8 bytes (int 64), which is the smallest block size in the
# Python heap object allocator. The heap block can allocate from 8 bytes to 512 bytes,
# but it needs to be a multiple of eight.

# Now let's discuss about the method 4, even though it looks quite efficient in terms
# of memory complexity, I would never use this in real life case since it overrides
# the input value.

# In python, dynamic types are passed as reference, not copy, so we need to be careful
# on how we manipulate our method arguments.

# Python has a pymalloc allocator optimized for small objects (smaller or equal to 512
# bytes) with a short lifetime. It uses memory mappings called “arenas” with a fixed
# size of 256 KiB. It falls back to PyMem_RawMalloc() and PyMem_RawRealloc() for
# allocations larger than 512 bytes
# (ref: https://docs.python.org/3.10/c-api/memory.html#the-pymalloc-allocator).


## Time details

# O(n^2): quadratic time (subset of polynomial time n^k), inneficient for large list
# because most modern computer can handle roughly 10^8 operations per second. If our
# list length (N) is of the size of 10^4, so n^2 = 10^8, which is borderline for
# acceptable performance, because we can process this 1 second. If N is 10^5, then
# N^2 = 10^10 (10 bi), which is 100 seconds (1.6 minutes). If N is 10^6, then N^2 =
# 10^12 (1 tri), which is 10,000 seconds (2.7 hours). The linear code of the last
# example here would take 0.01 seconds.

# Why O(n) is the most we can optimize here? If the output depends on every single
# input, your minimum time complexity is O(n). You cannot skip data and still get a
# correct sum. If you try to use a O(logn) approach, you would only look at roughly 2
# or 3 numbers out of 1,000. You would be missing 997 numbers, so your sum would be
# wrong.

## Other details

# prefix sum array or cumulative sum array

# On average, the sum function touches n/2 elements. Since you call this sum function
# n times. The math is: n×(n/2)=1/2(​n**2). That's why the sum is a bad implementatio
# because we are re-doing the calculation of [0:i] again and again.

# Instead, we can store the previous sum and add the next element to it.
# This way, we only loop through the array once, resulting in O(n) time complexity.

# About the sum in average being n/2 elements, this is because when we sum from 0 to i,
# i goes from 0 to n-1. So the average of i is (0 + (n-1)) / 2 = (n-1)/2 ~ n/2.

# In math terms, we are calculating the Sum of an Arithmetic Series (arithmetic
# progression). The series is: 0, 1, 2, 3, ..., (n-1).
# The formula is n/2(first term + last term).
# Here, first term is 0, last term is (n-1), and there are n terms.
# So the total sum is n/2(0 + (n-1)) = n(n-1)/2 ~ n^2/2.
# To find the average we divide by n, which gives us n/2.
