class Solution:
	def pushZerosToEnd(self,arr):
		non_zero_p = 0
		for i in range(len(arr)):
			if(arr[i]!=0):
				arr[non_zero_p] = arr[i]
				non_zero_p+=1 
		while(non_zero_p<len(arr)):
			arr[non_zero_p]=0
			non_zero_p+=1
			
input_str = input("Enter numbers separated by space: ")
arr = list(map(int, input_str.strip().split()))
sol = Solution()
sol.pushZerosToEnd(arr)
print("Array after pushing zeros to the end:")
print(arr)