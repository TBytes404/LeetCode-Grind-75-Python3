class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        word = zip(word1, word2)
        chars = (v for w in word for v in w)
        return "".join(chars) + word1[minLen:] + word2[minLen:]


sol = Solution()
out = sol.mergeAlternately("abc", "pqrs")
print(out)
