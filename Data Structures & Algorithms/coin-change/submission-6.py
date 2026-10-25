class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = deque([0])
        step = 0
        seen = [False] * (amount + 1)
        seen[0] = True
        while queue:
            step += 1
            for i in range(len(queue)):
                money = queue.popleft()
                for coin in coins:
                    if money + coin == amount:
                        return step
                    if money + coin > amount or seen[money + coin] == True:
                        continue
                    queue.append(money + coin)
                    seen[money + coin] = True
        return -1