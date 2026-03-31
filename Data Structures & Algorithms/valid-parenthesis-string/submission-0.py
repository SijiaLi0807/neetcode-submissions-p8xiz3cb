class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        如果遇到左括号，则将最小值和最大值分别加 1；
        如果遇到右括号，则将最小值和最大值分别减 1；
        如果遇到星号，则将最小值减 1，将最大值加 1。

        任何情况下，最少未匹配的左括号数量必须非负（_min），因此当最大值变成负数时，说明没有左括号可以和右括号匹配，返回 false。
        当最小值为 0 时，不应将_min继续减少(最少未匹配的左括号数量)，以确保最小值非负。
        遍历结束时，所有的左括号都应和右括号匹配，因此只有当最小值为 0 时，字符串 s 才是有效的括号字符串。
        '''
        _min, _max = 0, 0
        for i in s:
            if i == '(':
                _min +=1
                _max +=1
            elif i ==')':
                _min = max(_min-1,0)
                _max -=1 
                
            else:
                _min = max(_min-1,0)
                _max +=1
            if _max < 0:
                return False 
        return _min==0