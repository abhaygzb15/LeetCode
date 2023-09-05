class Solution(object):
    def isPalindrome(self, x):
        cpystr=str(x)
        cpystr2=cpystr[::-1]
        if(cpystr==cpystr2):
            return True
        else:
            return False
        
        
        