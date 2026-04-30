class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0, j = 0;
        int n = nums.size();
        int target = 0;
        while (j<n){
            target = nums[j];
            nums[i] = target;
            //++j;
            ++i;
            
            while (j<n && nums[j]==target){
                ++j;
            }

        }
        return i;

    }
};