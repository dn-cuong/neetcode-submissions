from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        visited = set()
        ans = 1
        while queue:
            ans += 1
            for q in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        new = word[:i] + j + word[i+1:]
                        if new == endWord and new in wordList:
                            return ans
                        if new not in visited and new in wordList:
                            queue.append(new)
                            visited.add(new)
        
        return 0

