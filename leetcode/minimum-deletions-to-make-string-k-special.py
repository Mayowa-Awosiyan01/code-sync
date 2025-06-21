class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = defaultdict(int)

        for i in word:
            freq[i]+=1

        freq = sorted(freq.items(), key=lambda kv: (kv[1], kv[0]))
        #print(freq)
        if len(freq) <2 or k>=len(word):
            return 0
        
        ans = len(word)
        for j in range(len(freq)):
            low = freq[j][1]
            curr =0
            for i in range(len(freq)):
                if freq[i][1] < low:
                    curr+=freq[i][1]
                
                elif freq[i][1] > low + k:
                    curr += freq[i][1] - low - k
            ans= min(ans,curr)
        
        return ans