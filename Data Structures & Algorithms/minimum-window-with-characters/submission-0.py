class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        nums_t = Counter(t)
        nums_s = Counter()
        ans_l, ans_r = -1, len(s) #ans_l初始化为-1，代表未找到可行的子字符串
        l = 0
        for r, value in enumerate(s): #移动子串右端点
            nums_s[value] += 1
            while nums_t <= nums_s: #要使用while，这样才能在右只移动一次，左端点缩短多次
                if r - l < ans_r - ans_l:
                    ans_r, ans_l = r, l 
                nums_s[s[l]] -= 1    #左端点字母移出子串
                l += 1 #若已满足条件，则移动子串左端点，缩短子串
        if ans_l == -1:
            return ""
        else:
            return s[ans_l: ans_r + 1] #左闭右开
        


        