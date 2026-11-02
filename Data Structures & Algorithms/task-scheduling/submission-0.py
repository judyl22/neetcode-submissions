class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1
        freq = [[-count, task] for task, count in freq.items()]
        heapq.heapify(freq)
        cooldown = deque()
        res = 0
        while freq or cooldown:
            res += 1
            if cooldown:
                add_new = cooldown.popleft()
                if add_new != '':
                    heapq.heappush(freq, add_new)
            if freq:
                count, task = heapq.heappop(freq)
                count += 1
                if count != 0:
                    while len(cooldown) < n:
                        cooldown.append('')
                    cooldown.append([count, task])
        return res