import collections


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        intervals = collections.deque(intervals)
        first = intervals.popleft()
        result_list = [first]
        while intervals:
            tmp_list = []
            stack = result_list.pop()
            queue = intervals.popleft()
            if stack[1] >= queue[0]:
                tmp_list += stack
                tmp_list += queue
                tmp_list.sort()
                result_list.append([tmp_list[0], tmp_list[-1]])
            else:
                result_list.append(stack)
                result_list.append(queue)

        return result_list