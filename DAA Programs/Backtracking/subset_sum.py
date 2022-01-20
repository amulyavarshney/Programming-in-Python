def SubsetSum(set, n, sum) :
   # Base Cases
   if (sum == 0) :
      return True
   if (n == 0 and sum != 0) :
      return False
   # ignore if last element is > sum
   if (set[n - 1] > sum) :
      return SubsetSum(set, n - 1, sum);
   # else,we check the sum
   # (1) including the last element
   # (2) excluding the last element
   return SubsetSum(set, n-1, sum) or SubsetSum(set, n-1, sum-set[n-1])
# main
set = [2, 14, 6, 22, 4, 8]
sum = 10
n = len(set)
if (SubsetSum(set, n, sum) == True) :
   print("Found a subset with given sum.")
else :
   print("No subset with given sum.")