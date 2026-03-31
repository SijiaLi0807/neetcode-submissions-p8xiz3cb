class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        m = len(freq)
        nextValid = [1] * m #nextValidi 表示其因冷却限制，最早可以执行的时间；
        rest = list(freq.values()) #剩余执行次数

        time = 0
        nt = len(tasks)
        for i in range(nt):
            time +=1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            time = max(time, minNextValid)

            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    if best == -1 or rest[j] > rest[best]:
                        best = j
            
            nextValid[best] = time + n + 1
            rest[best] -= 1
        return time