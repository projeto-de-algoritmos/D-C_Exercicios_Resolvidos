class Solution:
    def reverseBits(self, n: int) -> int:
        def divide_conquer(n,r,count):
            if n<1: # acabou
                return r<<(32-count) # completa 32 bits
            return divide_conquer(n>>1,(r<<1)|(n&1),count+1) # chamada recursiva
        return divide_conquer(n,0,0)
    
n = 43261596
solution = Solution()
result = solution.reverseBits(n)
print(f"Output: {result}")