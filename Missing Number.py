class Solution:
  #Code Starts here
  def Missing_Number(self,array,n):
    sum=n*(n+1)/2
    for i in range(n-1):
      sum-=array[i]
    return sum
n=int(input())
print("Enter numbers in range of 1 to",n)
array=list(map(int,input().split()))
print("The missing number in the given list of number is",int(Solution().Missing_Number(array,n)))
