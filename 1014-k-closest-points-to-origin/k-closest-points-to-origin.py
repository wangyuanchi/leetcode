class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points

        # use a max heap of size k
        # the key is the distance
        heap = []
        heapq.heapify(heap)

        for i in range(k):
            point = points[i]
            dist = self.distance(point[0], point[1])
            heapq.heappush(heap, (-dist, point)) # key is dist
        
        for i in range(k, len(points)):
            point = points[i]
            dist = self.distance(point[0], point[1])
            if dist < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist, point))

        res = []
        for elem in heap:
            res.append(elem[1])
        return res

    def distance(self, x, y):
        return math.sqrt(x**2 + y**2)