"""
Given: 𝑛 activities that require exclusive use of a common resource (e.g., scheduling use of SCDI 3302)
𝑆={𝑎_1,𝑎_2, …, 𝑎_𝑛 };𝑎_𝑖needs resource during [𝑠_𝑖, 𝑓_𝑖)
𝑠_𝑖:𝑠𝑡𝑎𝑟𝑡 𝑡𝑖𝑚𝑒;𝑓_𝑖:𝑓𝑖𝑛𝑖𝑠ℎ 𝑡𝑖𝑚𝑒;s_i<f_i
Assume: activities are sorted by finish times, i.e., 
𝑓_1≤𝑓_2≤…≤𝑓_(𝑛−1)≤𝑓_𝑛

Goal: Select the largest possible set of non-overlapping (i.e., mutually exclusive) activities
"""
# https://leetcode.com/problems/non-overlapping-intervals/description/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 1 # at least one interval from the intervals set is non-overlapping
        last_end = intervals[0][1]
        for start, end in intervals:
            if start >= last_end:
                count += 1
                last_end = end
        return n-count