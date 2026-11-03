class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        fail = False
        i = 0
        while i < n:
            if cost[i] > gas[i]:
                i += 1
                continue
            j = i
            tot_gas = 0
            fail = False
            while j < i + n:
                tot_gas = tot_gas + gas[j % n] - cost[j % n]
                if tot_gas < 0:
                    fail = True
                    break
                j += 1
            if fail:
                i = j
                continue
            return i
                