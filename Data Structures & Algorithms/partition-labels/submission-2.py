class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_dict = {}
        for i, char in enumerate(s):
            last_index_dict[char] = i

        end = last_index_dict[s[0]]
        size = 0
        res = []
        for i, char in enumerate(s):
            size += 1
            end = max(end, last_index_dict[char])
            if i == end:
                res.append(size)
                size = 0
        return res
