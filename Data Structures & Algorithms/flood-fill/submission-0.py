class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        filled = image[sr][sc]
        def dfs(image, sr, sc, visit):
            if sr >= len(image) or sc >= len(image[0]) or sr < 0 or sc < 0 or (sr,sc) in visit or image[sr][sc] != filled:
                return

            if image[sr][sc] == filled:
                image[sr][sc] = color 

            visit.add((sr,sc))

            dfs(image, sr +1, sc, visit)
            dfs(image, sr -1, sc, visit)
            dfs(image, sr, sc+1, visit)
            dfs(image, sr, sc-1, visit)

            return image
        dfs(image, sr, sc, set())

        return image