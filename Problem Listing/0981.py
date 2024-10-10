# https://leetcode.com/problems/time-based-key-value-store/
# 666 ms, 74.85 MB

class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.hashmap:
            left, mid, right = 0, 0, len(self.hashmap[key])-1
            while left <= right:
                mid = (left + right) // 2
                if self.hashmap[key][mid][1] == timestamp:
                    return self.hashmap[key][mid][0]
                elif self.hashmap[key][mid][1] > timestamp:
                    right = mid - 1
                else:
                    res = self.hashmap[key][mid][0]
                    left = mid + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
