class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        letterdict = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
            }
        res = []
        def backtracking(digits,index,path):
            n = len(digits)
            if index == n:
                res.append(path[:])
                return
            letters = letterdict[int(digits[index])]
            for i in range(len(letters)):
                path +=letters[i]
                backtracking(digits,index+1,path)
                path = path[:-1]
        backtracking(digits,0,'')
        return res