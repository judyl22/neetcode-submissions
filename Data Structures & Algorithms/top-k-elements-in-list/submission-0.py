class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        output = []
        sort_counts = dict(sorted(counts.items(), key=lambda item:item[1], reverse=True))
        for i in range(k):
            output.append(list(sort_counts)[i])
        return output