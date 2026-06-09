class Solution {
private:
    vector<int> path;
    vector<vector<int>> res;
    void backtracking(vector<int>& nums, vector<bool>& used){
        if (path.size()==nums.size()){
            res.push_back(path);
            return;
        }

        for (int i = 0; i < nums.size(); i++){
            if (i>0 && nums[i]==nums[i-1] && used[i-1]==false)
                continue;
            if (used[i]==true) continue;
            used[i]=true;
            path.push_back(nums[i]);
            backtracking(nums, used);
            used[i]=false;
            path.pop_back();
            
        }
    }

public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // 排序
        vector<bool> used(nums.size(), false);
        backtracking(nums, used);
        return res;
    }
};