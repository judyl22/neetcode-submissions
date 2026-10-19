class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backtrack(index):
            if index == len(s):
                res.append(curr.copy())
                return
            for end in range(index, len(s)):
                palindrome = True
                start = index
                temp_end = end
                while start <= temp_end:
                    if s[start] != s[temp_end]:
                        palindrome = False
                        break
                    start += 1
                    temp_end -= 1
                if palindrome == False:
                    continue
                curr.append(s[index:end+1])
                backtrack(end + 1)
                curr.pop()
        
        backtrack(0)
        return res