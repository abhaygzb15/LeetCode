class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=s.split()
        length=len(x)
        s=''
        for i in range(length-1,-1,-1):
            s=s+" "+x[i]
        return s.strip()
            
            
            
        