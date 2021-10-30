class Solution:
  #Code Starts here
  def Missing_Number(self,array,n):
    sum=n*(n+1)/2
    for i in range(n-1):
      sum-=array[i]
    return sum
N=int(intput())
array=[]
print("Enter numbers in range of 1 to",n)
for i in range(N-1):
  array[i]=int(input())
  print("The missing number in the given list of number is",Missing_Number(array,N))
