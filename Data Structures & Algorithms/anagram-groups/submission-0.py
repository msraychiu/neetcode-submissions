class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_map[sorted_s].append(s)
        
        result = []
        for k, v in anagram_map.items():
            result.append(v)

        return result
                
                

        
        
        