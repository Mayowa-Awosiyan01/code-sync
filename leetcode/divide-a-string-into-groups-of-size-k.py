class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> ans;
        for(int i=0;i<s.size();i=i+k){
            string curr;
            if(i+k<s.size()){
                curr.append(s.substr(i,k));
            }
            else{
                int remain = s.size()-i;
                curr.append(s.substr(i,remain));
                for(int j =0;j<k-remain;j++){
                    curr.push_back(fill);
                }
            }
            ans.push_back(curr);
            curr="";
        }

        return ans;
    }
};