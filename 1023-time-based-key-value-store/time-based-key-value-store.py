class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [(timestamp, value)]
        else:
            self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        
        timestamps = self.dict[key]
        l, r = 0, len(timestamps) - 1

        while l < r:
            m = l + (r - l) // 2

            if timestamps[m][0] == timestamp:
                return timestamps[m][1]

            if timestamps[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        if timestamps[l][0] <= timestamp:
            return timestamps[l][1]
        else:
            if timestamps[l][0] == timestamps[0][0]: # if first element
                return ""
            else:
                return timestamps[l - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)