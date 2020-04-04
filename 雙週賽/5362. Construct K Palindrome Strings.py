#Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.
#Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.
#23nd two weekly contest
#第2題

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        l = [0] * 26
        count = 0
        if len(s) == k:
            return 1
        if len(s) < k:
            return 0
        for i in range(len(s)):
            c = int(ord(s[i]) - 97)
            l[c] += 1
            if l[c] == 2:
                l[c] = 0
        
        for i in range(26):
            if (l[i] == 1):                   
                count += 1
        if count > k:
            return 0
        else :
            return 1