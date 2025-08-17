class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        groups = defaultdict(list)

        for word in strs:
            group = list(word)
            group.sort()
            group="".join(group)
            
            groups[group].append(word)
            
        
        for i in groups:
            ans.append(groups[i])
        
        return ans