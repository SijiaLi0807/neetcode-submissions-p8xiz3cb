class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<vector<int>> ans;
        if (n < 4){
            return ans;
        }
        sort(nums.begin(), nums.end());
        for (int a = 0; a < n-3; ++a){
            if (a > 0 && nums[a] == nums[a-1]){
                continue;
            }

            for (int b = a+1; b < n-2; ++b){
                if (b > a+1 && nums[b] == nums[b-1]){
                    continue;
                }

                long target_sum = (long) target - nums[a] - nums [b]; //强制类型转换
                int d = n - 1;

                for (int c = b+1; c < n-1; ++c){
                    if (c > b+1 && nums[c] == nums[c-1]){
                        continue;
                }
                    while(d>c && nums[d]+nums[c]>target_sum){
                        d-=1;
                    }
                    if (d == c){
                        break;
                    }
                    if (nums[d]+nums[c]==target_sum){
                        ans.push_back({nums[a], nums[b], nums[c], nums[d]});
                    } 
                } 
            }
        }
        return ans;
    }
};