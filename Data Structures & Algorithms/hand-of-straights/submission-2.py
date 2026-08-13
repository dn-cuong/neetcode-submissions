from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hashmap = Counter(hand)

        for x in hand:
            if hashmap[x] == 0:
                continue

            hashmap[x] -= 1

            count = 1
            c = x + 1

            while count < groupSize:
                if hashmap[c] == 0:
                    return False
                hashmap[c] -= 1
                c += 1
                count += 1

        return True



