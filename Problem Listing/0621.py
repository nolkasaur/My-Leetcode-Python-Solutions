# https://leetcode.com/problems/task-scheduler/
# 150 ms, 18.60 MB

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks) # [(k, v), ...] -> [(str, count)]
        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)
        time, queue = 0, deque()
        while maxHeap or queue:
            time += 1
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap) # subtract 1, but since the counts are negative, we add 1 instead
                if c: # if it's zero, do nothing because it's over
                    queue.append([c, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
