class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if(word.isupper()==True or word.islower()==True or word.istitle()==True):
            return True
        else:
            return False
        