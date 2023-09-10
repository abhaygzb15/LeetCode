class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        L=[]
        sum=0
        for i in jewels:
            L.append(stones.count(i))
        for i in L:
            sum=sum+i
        return sum
            
        