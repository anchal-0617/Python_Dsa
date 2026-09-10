class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        seen = set()

        for s in sentence:

            seen.add(s)

        if len(seen) == 26:

            return True
        return False       