class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        //comment
        vector<int> ans;
        for(int i=0; i<nums.size();i++){
            for(int j=i-k;j<i+k+1;j++){
                if(j<0){
                    j=0;
                }
                if(j >=nums.size()){
                    break;
                }
                if(nums[j]==key){
                    ans.push_back(i);
                    break;
                }
            }
        } 

        return ans;
    }
};