class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        res = n = len(position)
        time = [(target - cars[i][0])/cars[i][1] for i in range(n)]
        stack = []
        for i in range(n):
            while stack and time[i] >= time[stack[-1]]:
                stack.pop()
                res -= 1
            stack.append(i)
        return res
        