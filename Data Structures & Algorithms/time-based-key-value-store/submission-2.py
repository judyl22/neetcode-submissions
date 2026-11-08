class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = [(timestamp, value)]
        else:
            self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ''
        val_arr = self.dictionary[key]
        if val_arr[0][0] > timestamp:
            return ''
        n = len(val_arr)
        left = 0
        right = n - 1
        closest = float('-inf')
        res = ''
        while left <= right:
            mid = (left + right) // 2
            if val_arr[mid][0] == timestamp:
                return val_arr[mid][1]
            if val_arr[mid][0] < timestamp:
                if val_arr[mid][0] > closest:
                    closest = val_arr[mid][0]
                    res = val_arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

        
