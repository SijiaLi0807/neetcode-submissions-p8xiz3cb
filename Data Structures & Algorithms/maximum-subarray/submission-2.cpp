class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = INT_MIN;
        int dp = 0;

        for (int i = 0; i< nums.size(); i++){
            dp = max(dp,0) + nums[i];
            ans = max(ans, dp);
        }
        return ans;
    }
};