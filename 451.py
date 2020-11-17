#451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        string_dict = {}
        for i in s:
            if i in string_dict:
                string_dict[i] += 1
            else:
                string_dict[i] = 1
        out = [i[0] * i[1] for i in sorted(string_dict.items(), key=lambda x: x[1], reverse=True)]
        out = ''.join(out)
        return out
