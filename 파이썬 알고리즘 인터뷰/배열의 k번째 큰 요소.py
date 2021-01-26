import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
            
        return heapq.heappop(nums)

    def findKthLargest(self, nums: list, k: int)-> int:
        heap = []
        for num in nums:
            heapq.heapify(heap, -num)
        for _ in range(1, k):
            heapq.heappop(heap)
        return -heapq.heappop(heap)
        