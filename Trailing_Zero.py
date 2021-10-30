class Solution:
  def Trailing_Zero(self,N):
    temp=N
    trail=0
    while temp:
       trail=temp//5
       temp//=5
    return trail
N=int(input())
print("The number of trailing zeros in the factorial of",N,"are:",Solution().Trailing_Zero(N))
