class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        counts = Counter(hand)
        heap = []
        count_dict = {}
        for num, count in counts.items():
            heapq.heappush(heap, num)
            count_dict[num] = count
        
        print(heap)
        print(count_dict)
        while heap:
            if heap[0] not in count_dict:
                heapq.heappop(heap)
                continue
            smallest = heap[0]
            curr_group_size = 0
            while curr_group_size < groupSize:
                if smallest in count_dict:
                    count_dict[smallest] -= 1
                else:
                    return False
                if count_dict[smallest] == 0:
                    count_dict.pop(smallest)
                smallest += 1
                curr_group_size += 1
        return True
                