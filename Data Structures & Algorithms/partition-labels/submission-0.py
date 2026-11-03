class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = [i, i]
            if char in first:
                first[char][1] = i
        intervals = list(first.values())

        res = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            if res and start < res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(interval)
        res_len = []
        for start, end in res:
            res_len.append(end - start + 1)
        return res_len

        