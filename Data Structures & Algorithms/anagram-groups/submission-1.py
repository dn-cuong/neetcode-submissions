class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            alphabet = [0] * 26
            for x in strs[i]:
                alphabet[ord(x) - ord('a')] += 1
            if tuple(alphabet) in hashmap:
                hashmap[tuple(alphabet)].append(strs[i])
            else:
                hashmap[tuple(alphabet)] = [strs[i]]
        return [x for i,x in hashmap.items()]