class Solution:
    def isNumber(self, s: str):
        try:
            float(s)
            if "inf" in s.lower():
                return False
            return True
        except:
            return False
