class Solution {
public:
    int possibleStringCount(string word) {
        int ans = 1;
        for(int i =0; i<word.size()-1;i++){
            if(word.at(i) == word.at(i+1)){
                ans++;
            }
        }

        return ans;
    }
};