class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        output = output + str(len(strs)) + '.'
        long_str = ''
        for one_str in strs:
            one_len = str(len(one_str))
            output = output + one_len + '.'
            long_str = long_str + one_str
        output = output + long_str
        return output
        

    def decode(self, s: str) -> List[str]:
        arr_len = ''
        for i, c in enumerate(s):
            if c == '.':
                break
            arr_len = arr_len + c
        arr_len = int(arr_len)
        s = s[i+1:]
        len_arr = []
        while len(len_arr) != arr_len:
            one_len = ''
            for i, c in enumerate(s):
                if c == '.':
                    break
                one_len = one_len + c
            one_len = int(one_len)
            len_arr.append(one_len)
            s = s[i+1:]
        output = []
        for one_len in len_arr:
            one_str = ''
            for i, c in enumerate(s):
                if i == one_len:
                    break
                one_str = one_str + c
            output.append(one_str)
            s = s[i:]
        return output