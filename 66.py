#66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        digits[-1] += 1
        while (digits[i])%10 == 0:
            digits[i] = digits[i]%10
            if abs(i - 1) > len(digits):
                digits = [1] + digits
            else:
                digits[i - 1] += 1
            i -= 1
        return digits
