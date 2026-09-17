class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hashmap[key]:
            return ""

        res = ""
        l, r = 0, len(self.hashmap[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.hashmap[key][m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
                res = self.hashmap[key][m][0]

        return res
