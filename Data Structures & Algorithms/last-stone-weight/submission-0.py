class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            light = heapq.heappop(stones)
            heavy = heapq.heappop(stones)
            if light == heavy:
                continue
            else:
                heapq.heappush(stones, light - heavy)
        if not stones:
            return 0
        return -heapq.heappop(stones)
