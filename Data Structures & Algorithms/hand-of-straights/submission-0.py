class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        hand_dict = {}
        for num in hand:
            if num not in hand_dict:
                hand_dict[num] = 1
            else:
                hand_dict[num] += 1
        while hand_dict:
            smallest = min(hand_dict)
            curr_group = 0
            while curr_group < groupSize:
                if smallest not in hand_dict:
                    return False
                hand_dict[smallest] -= 1
                if hand_dict[smallest] == 0:
                    hand_dict.pop(smallest)
                smallest += 1
                curr_group += 1
        return True