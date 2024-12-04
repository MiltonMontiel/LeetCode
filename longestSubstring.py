class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int: 
        visited = {}
        startOfSubstring = 0
        largestSubstringLen = 0

        for idx, c in enumerate(s):
            j = visited.get(c,-1)
            
            if j >= startOfSubstring: 
                startOfSubstring = j + 1
            else: 
                newLargest = idx - startOfSubstring + 1
                if newLargest > largestSubstringLen: 
                    largestSubstringLen = newLargest
            visited[c] = idx


        return largestSubstringLen