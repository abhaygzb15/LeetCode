class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        res=haystack.find(needle)
        if(res!=-1):
            return res
        else:
            return -1
        