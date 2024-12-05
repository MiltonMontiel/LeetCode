class Solution:
    def matches(self, s: str, p: str, i: int, j: int, memory) -> bool:
        # Base cases 
        if i >= len(s) and j >= len(p): 
            return True 
        elif j >= len(p): 
            return False 
        
        # Check if we have already computed the result
        if memory[i][j] is not None: 
            return memory[i][j]

        matches = i < len(s) and (s[i] == p[j] or p[j] == '.')
        isAMatch = None

        if j < len(p) - 1 and p[j+1] == "*": 
            isAMatch = (matches and self.matches(s,p,i+1,j,memory) or self.matches(s,p,i,j+2,memory))
        else: 
            isAMatch = matches and self.matches(s,p,i+1,j+1,memory)

        # We register the result in memory
        memory[i][j] = isAMatch

        return isAMatch 

    def isMatch(self, s: str, p: str) -> bool:
        memory = [[None] * (len(p)) for i in range(len(s)+1)]
        return self.matches(s,p,0,0,memory)