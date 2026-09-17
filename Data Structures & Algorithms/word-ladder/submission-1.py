from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([beginWord])
        visited = {beginWord}
        level = 1
        
        if endWord not in wordList:
            return 0

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1:]

                        if new_word == endWord:
                            return level + 1

                        if new_word in wordList and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)

            level += 1

        return 0