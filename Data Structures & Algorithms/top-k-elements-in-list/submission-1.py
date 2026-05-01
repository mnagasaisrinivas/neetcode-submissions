class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dk : dict[int, int] = {}
        return_list : list[int] = []

        for i in nums:
            if i in dk:
                dk[i] += 1
            
            else:
                dk[i] = 1

        new_dk : dict[int, int] = dict(sorted(dk.items(), key = lambda x : x[1], reverse = True))
        
        return_list : list[int] = []
        
        for i in new_dk.items():
            return_list.append(i[0])
            
            if len(return_list) == k:
                break
        
        return return_list