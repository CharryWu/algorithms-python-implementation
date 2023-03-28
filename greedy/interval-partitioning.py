from typing import List
"""
Lecture j starts at 𝑠_𝑗and finishes at 𝑓_𝑗
Goal: Find minimum #classrooms to schedule all lectures
so that no two occur at the same time in the same classroom

Defn: The depth of a set of open intervals is the max num that contain any given time
Key observation: #classrooms needed >= depth
Example: Depth of intervals = 3 -> schedule is optimal

Greedy choice: Consider lectures in increasing order of start time: assign lecture to any compatible classroom
If we can't find any compatible classroom, create a new classroom.

Let d = #classrooms that the greedy algorithm allocates
Classroom d is opened because we needed to schedule a job, say j, that is incompatible with all d-1 other classrooms

Since we sorted by start time, all these incompatibilities are caused by lectures
that start no later than 𝑠_𝑗
Thus, we have d lectures overlapping at time 𝑠_𝑗+𝜖
Key observation: all schedules use ≥𝑑 classrooms

"""
# Same as https://leetcode.com/problems/meeting-rooms-ii/
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        count = 0

        heap = []  # (EndTime, RoomId)
        roomid = 0
        for start, end in intervals:
            if len(heap) == 0 or start < heap[0][0]:
                roomid += 1
                heapq.heappush(heap, (end, roomid))
            else:
                last_end, roomid = heapq.heappop(heap)
                heapq.heappush(heap, (end, roomid))

        return len(heap)


    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
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
