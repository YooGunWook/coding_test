import collections
import heapq

class Solution:
    def solution(self, nums: list, k: int) -> list:
        hash = collections.Counter(nums)
        result = []
        for i in hash:
            if hash[i] < 2:
                continue
            else:
                result.append(i)
        return result

    def heap_solution(self, nums: list, k: int) -> list:
        freqs = collections.Counter(nums)
        freqs_heap = []
        topk = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

    def pythonic_solution(self, nums: list, k: int)-> list:
        return list(zip(*collections.Counter(nums).most_common(2)))[0]


if __name__ == "__main__":
    print(Solution().solution([1, 1, 1, 2, 2, 3], 2))

