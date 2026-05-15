class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Distance list:
        distance = [math.sqrt(x[0]**2 + x[1]**2) for x in points]
        combined = list(zip(distance, points))
        count = 0
        heapq.heapify(combined)
        ans = []
        while count < k:
            sol, val = heapq.heappop(combined)
            ans.append(list(val))
            count +=1
        return ans

