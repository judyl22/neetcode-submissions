class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dic = {}
        for str in strs:
            arr = []
            for c in str:
                arr.append(c)
            arr.sort()
            sort_str = ''.join(arr)
            if sort_str not in char_dic:
                char_dic[sort_str] = [str]
            else:
                char_dic[sort_str].append(str)
        output = []
        for key, val in char_dic.items():
            output.append(val)
        return output