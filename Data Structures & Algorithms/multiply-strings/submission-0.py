class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        arr = [0] * (m+n)
        for i in range(m-1,-1,-1):
            x = int(num1[i])
            for j in range(n-1,-1,-1):
                arr[i+j+1] += x * int(num2[j]) #模仿竖式计算
                '''
                 11
                *11
                ----
               0011
               011
                ----
               0121
                '''

        for i in range(m+n-1,0,-1):
            arr[i-1] += arr[i]//10
            arr[i] %= 10
        
        index = 0 if arr[0] else 1
        ans = ''.join(str(x) for x in arr[index:])
        return ans

        