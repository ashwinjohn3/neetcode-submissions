class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # init maxHeap 
        maxHeap = [-x for x in stones]
        print(stones)
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            largest = heapq.heappop(maxHeap)
            largest_2 = heapq.heappop(maxHeap)
            new_stone = largest - largest_2
            heapq.heappush(maxHeap, new_stone)
        
        return -1*maxHeap[0] if maxHeap else 0

        