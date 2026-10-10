class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = {}
        for i in range(len(position)):
            pairs[position[i]] = speed[i]
        # print(pairs)
        pairs = dict(sorted(pairs.items()))
        # print(pairs)
        times = []
        for pos, sp in pairs.items():
            time = (target - pos) / sp
            times.append(time)
        # print(times)
        fleet = 1
        last_time = times.pop()
        while times:
            time = times.pop()
            # print(last_time)
            # print(time)
            if time > last_time:
                # print('add')
                fleet += 1
                last_time = time
            else:
                last_time = max(last_time, time)
                # print('not add')
            # print(times)
        return fleet