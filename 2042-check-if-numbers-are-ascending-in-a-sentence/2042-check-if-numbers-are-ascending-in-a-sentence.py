class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L=[]
        for i in s:
            x=s.split()
        for i in x:
            if(i.isdigit()==True):
                L.append(int(i))
        for i in range(1, len(L)):
            if L[i] <= L[i - 1]:
                return False
        
        return True
                    