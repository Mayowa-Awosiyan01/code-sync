class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"M": 1000, "D": 500,"C":100, "L":50,"X": 10,
        "V": 5, "I":1}

        ans =0
        prev = "M"

        for i in s:
            if values[prev] < values[i]:
                ans-=values[prev]*2
                ans+=values[i]
            else:
                ans+= values[i]
            prev = i

        return ans