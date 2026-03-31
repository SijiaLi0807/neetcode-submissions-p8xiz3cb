class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        if m > len(s2):
            return False

        cnt_s1 = Counter(s1)  # 统计 s1 的每种字母的出现次数
        cnt_t = Counter()  # 对于 s2 的长为 m 的子串 t，统计 t 的每种字母的出现次数
        for i, c in enumerate(s2):
            # 1. 进入窗口
            cnt_t[c] += 1
            if i < m - 1:  # 窗口大小不足 m
                continue
            # 2. 判断子串 t 的每种字母的出现次数是否均与 s1 的相同
            if cnt_t == cnt_s1:
                return True
            # 3. 离开窗口，为下一个循环做准备
            cnt_t[s2[i - m + 1]] -= 1
        return False