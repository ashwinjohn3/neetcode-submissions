import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(self.get_absolute_distance(points[x], [0,0]), points[x]) for x in range(len(points))]
        print(min_heap)
        heapq.heapify(min_heap)
        k_closest_points = []
        for i in range(k):
            k_closest_points.append(heapq.heappop(min_heap)[-1])
        return k_closest_points

    def get_absolute_distance(self, point1: List[int], point2: List[int]):
        return abs(math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

