class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m -1, j = n-1;
        while(i>=0 && j >=0){
            if(nums2[j]>=nums1[i]){
                nums1[i+j+1] = nums2[j];
                --j;
            } else {
                nums1[i+j+1] = nums1[i];
                --i;
            }
        }
        
        while (j >=0){ //cpp不支持多个下标，只能用循环
            nums1[j] = nums2[j];
            --j;
        }
    }
};