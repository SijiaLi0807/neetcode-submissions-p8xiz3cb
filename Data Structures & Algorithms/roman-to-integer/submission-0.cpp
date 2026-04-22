class Solution {
private:
        unordered_map<char, int> symVals = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

public:
    int romanToInt(string s) {
        int ans = 0;
        int n = s.length();
        
        for (int i = 0; i < n; ++i){
            int val = symVals[s[i]];
            if (i < n-1 && val < symVals[s[i+1]]){
                ans -= val;
            }
            else{
                ans += val;
            }
        }
        return ans;
    }
};