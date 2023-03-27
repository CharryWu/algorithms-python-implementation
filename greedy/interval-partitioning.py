from typing import List
# https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(list(map(lambda x: x[0], intervals)))
        ends = sorted(list(map(lambda x: x[1], intervals)))

        allocated = 0
        start_ptr = end_ptr = 0

        while start_ptr < len(intervals):
            if ends[end_ptr] <= starts[start_ptr]:
                allocated -= 1
                end_ptr += 1

            start_ptr += 1
            allocated += 1
        return allocated
