from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hashmap = Counter(hand)

        while hashmap:
            x = min(hashmap)

            for i in range(groupSize):
                if hashmap[x + i] == 0:
                    return False

                hashmap[x + i] -= 1

                if hashmap[x + i] == 0:
                    del hashmap[x + i]

        return True