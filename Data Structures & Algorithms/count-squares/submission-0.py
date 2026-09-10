class CountSquares:

    def __init__(self):
        self.hashmap = {}

    def add(self, point: List[int]) -> None:
        self.hashmap[tuple(point)] = self.hashmap.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        query_x, query_y = point[0], point[1]

        res = 0
        for pt in self.hashmap:
            pt_x, pt_y = pt
            dx, dy = query_x - pt_x, query_y - pt_y

            # Check if the point is diagonal to query point
            if dx != 0 and abs(dx) == abs(dy):
                target1, target2 = (query_x - dx, query_y), (query_x, query_y - dy)

                if target1 in self.hashmap and target2 in self.hashmap:
                    res += (self.hashmap[pt] * self.hashmap[target1] * self.hashmap[target2])
        
        return res

