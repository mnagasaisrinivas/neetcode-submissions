class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [[strs[0]]]

        sorted_strs : list[str] = []

        for key, value in enumerate(strs):
            sorted_strs.append((key, "".join(sorted(value))))
            
        sorted_strs.sort(key = lambda x : x[1])
            
        return_str : list[str] = []
        temp : str = ""
        list_index : int = 0
        
        for i in range(len(sorted_strs)):
            if i == 0:
                temp = sorted_strs[i][1]
                return_str.insert(list_index, [strs[sorted_strs[i][0]]])
                continue
                
            if sorted_strs[i][1] == temp:
                return_str[list_index].append(strs[sorted_strs[i][0]])
                
            else:
                temp = sorted_strs[i][1]
                list_index += 1
                return_str.insert(list_index, [strs[sorted_strs[i][0]]])
                
        return_str.sort(key=len)        
        
        return return_str
        
    