class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> cnt {
            {0,1}
        }; // s[0] = 0单独统计
        int ans = 0, s = 0;
        for (int n: nums){
            s += n;
            ans += cnt[s-k];
            cnt[s]++;
        }
        return ans;
    }
};