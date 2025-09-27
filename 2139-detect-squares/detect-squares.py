class DetectSquares:

    def __init__(self):
        # Key is x, value is a dictionary (where the key is y, and the value is the freq)
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        if x not in self.points:
            self.points[x] = {}
        if y not in self.points[x]:
            self.points[x][y] = 1
        else:
            self.points[x][y] += 1
    
    # To form a square, there must be at least 1 point on the same x,
    # and if we find the point, there are only 2 remaining possible squares.
    def count(self, point: List[int]) -> int:
        x1, y1 = point[0], point[1]
        if x1 not in self.points:
            return 0
            
        total = 0
        
        for y2, freq0 in self.points[x1].items():
            # Ignore currently checked point as it leads to square of side length 0
            if y2 == y1:
                continue
                
            length = y2 - y1

            # Right now, we have freq number of (x1, y2) points
            # Square 1 points: (x1 + length, y1), (x1 + length, y2)
            if x1 + length in self.points:
                if y1 in self.points[x1 + length] and y2 in self.points[x1 + length]:
                    freq1 = self.points[x1 + length][y1]
                    freq2 = self.points[x1 + length][y2]
                    total += freq0 * freq1 * freq2

            # Square 2 points: (x1 - length, y1), (x1 - length, y2)
            if x1 - length in self.points:
                if y1 in self.points[x1 - length] and y2 in self.points[x1 - length]:
                    freq1 = self.points[x1 - length][y1]
                    freq2 = self.points[x1 - length][y2]
                    total += freq0 * freq1 * freq2
            
        return total
