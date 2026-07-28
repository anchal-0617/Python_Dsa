class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        

        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else :
            idx = 2

        count = 0
        for item in items:
            if item[idx] == ruleValue:
                count += 1

        return count        


