from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
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
        # hashmap
        # 1 2 2 3 3 4 4 5

        # 1: 1 -> 0
        # 2: 2 -> 1
        # 3: 2 -> 1
        # 4: 2 -> 1 
        # 5: 1



