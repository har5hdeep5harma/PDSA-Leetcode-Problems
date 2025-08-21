class Solution(object):
    def reverseVowels(self, s):
        s = list(s)  
        vowels = [c for c in s if c in 'aeiouAEIOU']  
        vowels.reverse()  
        
        j = 0
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                s[i] = vowels[j]
                j += 1
        return "".join(s)  