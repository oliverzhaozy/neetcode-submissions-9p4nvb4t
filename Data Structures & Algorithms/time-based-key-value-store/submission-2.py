class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        l, r = 0, len(self.hashmap[key]) - 1
        res_m = -1
        while l <= r:
            m = (l + r) // 2
            timestamp_prev = self.hashmap[key][m][1] 
            
            if timestamp_prev > timestamp:
                r = m - 1
            else:
                res_m = max(res_m, m)
                l = m + 1
        
        return self.hashmap[key][res_m][0] if res_m != -1 else ""