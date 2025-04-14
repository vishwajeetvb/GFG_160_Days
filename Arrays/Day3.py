class Solution:
    def reverseArray(self, arr):
        start=0
        end=len(arr)-1
        while(start<end):
            temp = arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1

user_input = input("Enter elements of the array separated by spaces: ")
arr = list(map(int, user_input.strip().split()))
sol = Solution()
sol.reverseArray(arr)
print("Reversed array:", arr)