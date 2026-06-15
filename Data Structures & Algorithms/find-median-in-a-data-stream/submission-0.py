from _heapq import heappop, heappushpop
class MedianFinder:

    def __init__(self):
        self.min_heap = [] # stores the larger half of the stream 
        self.max_heap = [] # stores the smaller half of the stream
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, -heappushpop(self.max_heap, -num)) 
        if len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if not self.min_heap:
            return 0
        elif len(self.min_heap) - len(self.max_heap) == 1:
            return self.min_heap[0]
        else:
            print(self.min_heap)
            print(self.max_heap)
            return (self.min_heap[0] - self.max_heap[0])/2