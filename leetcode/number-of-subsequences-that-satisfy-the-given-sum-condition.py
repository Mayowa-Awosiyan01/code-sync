class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        const int MOD = 1e9 + 7;
        vector<int> powers(nums.size(), 1);
        for (int i = 1; i < nums.size(); ++i){
            powers[i] = (powers[i - 1] * 2) % MOD;
        }

        int big = nums.size()-1;
        int small = 0;
        
        stable_sort(nums.begin(), nums.end());

        long ans=0;
       
        while(nums.size() > small && small<=big){
            if(nums.at(small) +nums.at(big) <=target){
                
                ans= ans + powers[big-small];
                small++;
            }
            else{
                big--;
                                
            }
        }

        


        ;
        return ans % MOD;
    }
};