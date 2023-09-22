class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        set1=set(ransomNote)
        set2=set(magazine)
        list1=list(set1)
        list2=list(set2)
        found_chars = set()  
        for i in list1:
            if i in list2 and ransomNote.count(i) <= magazine.count(i):
                found_chars.add(i) 
        return len(found_chars) == len(set1)


