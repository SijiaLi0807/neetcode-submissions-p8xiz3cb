class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        // 这里的 & 是引用，
        // vector<int>& nums 表示：nums 是传进来的那个 vector<int> 的别名，不是拷贝。
        int target = nums.size() / 3;
        vector<int> ans;
        unordered_map<int,int> cnt;

        for (auto & v: nums){ 
            //为什么auto?因为 C++ 里很多类型写出来很长，auto 可以让编译器自动推断类型，代码更简洁
            cnt[v]++;
        }

        for (auto & v: cnt){
            if (v.second > target){ //.first是key, .second是value
                ans.push_back(v.first);
            }

        }
        return ans;
    }   
};
