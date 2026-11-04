class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_dict = {i : [] for i in range(n)}
        for from_stop, to_stop, price in flights:
            flight_dict[from_stop].append((to_stop, price))
        cheapest = {}
        cheapest[(src, 0)] = 0
        min_heap = []
        for to_stop, price in flight_dict[src]:
            heapq.heappush(min_heap, (price, to_stop, 1))
        while min_heap:
            price, from_stop, stop = heapq.heappop(min_heap)
            if (from_stop, stop) in cheapest:
                continue
            if stop > k + 1:
                continue
            cheapest[(from_stop, stop)] = price
            for to_stop, to_price in flight_dict[from_stop]:
                new_price = price + to_price
                heapq.heappush(min_heap, (new_price, to_stop, stop + 1))
        min_price = float('inf')
        for i in range(k + 2):
            if (dst, i) in cheapest:
                min_price = min(min_price, cheapest[(dst, i)])
        return min_price if min_price != float('inf') else -1
