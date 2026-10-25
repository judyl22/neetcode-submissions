class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        queue = deque([0])
        while queue:
            for i in range(len(queue)):
                index = queue.popleft()
                for word in wordDict:
                    length = len(word)
                    if index + length > n or dp[index + length]:
                        continue
                    if s[index:index+length] == word:
                        dp[index + length] = True
                        queue.append(index + length)
        return dp[n]