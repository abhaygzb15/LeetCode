class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits=[]
        for i in s:
            if(i.isdigit()==True):
                digits.append(int(i))
        digits=set(digits)
        if(len(digits)<2):
            return -1
        else:
            digits=list(digits)
            digits.sort()
            return digits[-2]