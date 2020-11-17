#1545. Find Kth Bit in Nth Binary String

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def create_string(n):
            if n == 1:
                return "0"
            s = create_string(n-1)
            s_invert = s.replace("0", "2").replace("1", "0").replace("2", "1")
            s = s + "1" + s_invert[::-1]
            return s
        s = create_string(n)
        return s[k-1]
