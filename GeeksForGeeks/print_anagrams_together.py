from collections import defaultdict
class Solution:
    def Anagrams(self, words, n):
        d = defaultdict(list)
        for word in words:
            key = tuple(sorted(word))
            d[key].append(word)
        return d.values()