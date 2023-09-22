class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum1=0
        c=-1
        L=[]
        for i in accounts:
            c=c+1
            for j in range(len(i)):
                sum1=sum1+int(accounts[c][j])
            L.append(sum1)
            sum1=0
        return max(L)
            
            
        