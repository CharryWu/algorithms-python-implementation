# https://leetcode.com/problems/find-peak-element/description/
"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: # single element is peak
            return 0
        if n > 1: # check if nums leftmost and rightmost peak
            if nums[0] >= nums[1]:
                return 0
            if nums[n-1] >= nums[n-2]:
                return n-1

        # check remaining
        left, right = 1, n-2

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid   # if mid == peak ( case 2 )
            elif nums[mid] < nums[mid-1]:
                right = mid - 1 # downward slope and search space left side ( case 1)
            elif nums[mid] < nums[mid+1]:
                left = mid + 1 # upward slope and search space right side ( case 3 )
        return left