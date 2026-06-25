class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for x in strs:
            sorted_str = sorted(x)
            if tuple(sorted_str) in dct:
                dct[tuple(sorted_str)].append(x)
            else:
                dct[tuple(sorted_str)] = [x]
        return [dct[x] for x in dct]