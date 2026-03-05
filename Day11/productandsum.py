class Solution:
    def subtractProductAndSum(self, n: int) -> int:
         prod = 1
         s = 0
        
         for d in str(n):
             prod *= int(d)
             s += int(d)
            
         return prod - s
