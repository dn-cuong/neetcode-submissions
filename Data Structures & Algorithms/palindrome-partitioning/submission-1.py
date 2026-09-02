class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Store all valid palindrome partitions
        res = []

        def backtracking(start, path):
            # If we have reached the end of the string,
            # we found one complete partition.
            if start == len(s):
                res.append(path.copy())
                return

            # Try every possible substring starting at `start`
            for end in range(start, len(s)):
                # Get the substring from start to end
                substring = s[start:end + 1]

                # Check if the substring is a palindrome
                # A palindrome is the same forwards and backwards.
                if substring == substring[::-1]:

                    # Choose: add this palindrome to our current partition
                    path.append(substring)

                    # Explore: continue partitioning from the next character
                    backtracking(end + 1, path)

                    # Undo: remove the last substring
                    # so we can try a different partition.
                    path.pop()

        # Start backtracking from index 0 with an empty partition
        backtracking(0, [])

        # Return all possible palindrome partitions
        return res