class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        query_dict = {}
        for i, query in enumerate(queries):
            if query not in query_dict:
                query_dict[query] = [i]
            else:
                query_dict[query].append(i)
        res = [0] * len(queries)
        queries.sort()

        min_heap = [] # each element in the min_heap will be (length, end)
        next_int = 0
        for query in queries:
            i = 0
            while res[query_dict[query][i]] != 0:
                i += 1
            query_index = query_dict[query][i]

            while next_int < len(intervals) and intervals[next_int][0] <= query:
                interval = intervals[next_int]
                start, end = interval
                heapq.heappush(min_heap, (end - start + 1, end))
                next_int += 1
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            if not min_heap:
                res[query_index] = -1
            else:
                length, end = min_heap[0]
                res[query_index] = length
        return res
        