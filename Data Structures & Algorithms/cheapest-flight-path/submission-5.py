class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_dict = {i : [] for i in range(n)}
        for from_i, to, price in flights:
            flight_dict[from_i].append((to, price))
        cheapest = {}
        cheapest[src] = 0
        least_stop = {i : float('inf') for i in range(n)}
        price_heap = []
        for to, price in flight_dict[src]:
            heapq.heappush(price_heap, (price, to, 1))
        while price_heap:
            price_from, come_from, stop = heapq.heappop(price_heap)
            if come_from in cheapest and least_stop[come_from] <= stop:
                continue
            if stop > k + 1:
                continue
            cheapest[come_from] = min(price_from, cheapest.get(come_from, float('inf')))
            least_stop[come_from] = stop
            for to, price_to in flight_dict[come_from]:
                new_price = price_to + price_from
                heapq.heappush(price_heap, (new_price, to, stop + 1))
        if dst not in cheapest:
            return -1
        return cheapest[dst]
                
