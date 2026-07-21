class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0

        deadset = set(deadends) #用set存储deadends，减少判断数字是否为死亡数字的时间（o(1)）

        if '0000' in deadset:
            return -1
        
        def num_prev(x: str) -> str:
            '''
            return the previous slot.
            '''
            return "9" if x == "0" else str(int(x) - 1)
        
        def num_succ(x: str) -> str:
            '''
            return the next slot.
            '''
            return "0" if x == "9" else str(int(x) + 1)

        # 枚举 status 通过一次旋转得到的数字
        def bfs(status: str) -> Generator[str, None, None]:
            s = list(status)
            result = []

            for i in range(4):
                #没有follow题解，这样比较好理解
                num = s[i]

                s[i] = num_prev(num)
                result.append("".join(s))

                s[i] = num_succ(num)
                result.append("".join(s))

                s[i] = num #改回去

            return result
        
        q = deque( [ ('0000', 0) ] ) #bfs必备的queue
        visited = {'0000'} #bfs必备的visited

        while q:
            status, step = q.popleft()
            for next_status in bfs(status):
                if next_status in deadset or next_status in visited:
                    continue
                if next_status == target:
                    return step+1
                q.append([next_status, step+1])
                visited.add(next_status)

        return -1