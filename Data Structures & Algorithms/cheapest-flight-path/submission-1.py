class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {i : [] for i in range(n)}
        for flight in flights:
            from_i, to_i, price_i = flight
            adj_list[from_i].append((to_i, price_i))
        queue = deque()
        for src_adj, price in adj_list[src]:
            queue.append((src_adj, price, 1)) # 1 as the 1st stop
        min_price_stop = {i : float('inf') for i in range(n)}
        min_price_stop[src] = 0
        while queue:
            come_from, price_come, stop = queue.popleft()
            if come_from != dst and stop >= k + 1:
                continue
            if min_price_stop[come_from] <= price_come:
                continue
            min_price_stop[come_from] = price_come
            if come_from == dst:
                continue
            for go_to, price_to in adj_list[come_from]:
                new_price = price_come + price_to
                if min_price_stop[go_to] <= new_price:
                    continue
                queue.append((go_to, new_price, stop + 1))
        return min_price_stop[dst] if min_price_stop[dst] != float('inf') else -1

            
            

