class Solution(object):
    def isValid(self, word):
        l=0
        m=0
        k=0
        al=['a', 'e', 'i', 'o', 'u']
        if len(word)>=3:
            if word.isalnum():
                for n in word.lower():
                    if n in al:
                        l+=1
                    elif n.isnumeric():
                        m+=1
                    else:
                        k+=1
        if l>=1 and k>0:
            return True
        else:
            return False

            