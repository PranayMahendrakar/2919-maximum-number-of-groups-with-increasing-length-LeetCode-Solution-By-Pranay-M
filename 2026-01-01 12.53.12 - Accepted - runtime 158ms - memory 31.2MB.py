class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        
        groups = 0
        total = 0
        
        for limit in usageLimits:
            total += limit
            # Can we form one more group?
            # Need 1+2+...+(groups+1) total elements
            needed = (groups + 1) * (groups + 2) // 2
            if total >= needed:
                groups += 1
        
        return groups