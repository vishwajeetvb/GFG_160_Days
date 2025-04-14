class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def reverse(self, arr, start, end):
        while(start<end):
            temp=arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1
    def rotateArr(self, arr, d):
        d=d%len(arr)
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,len(arr)-1)
        self.reverse(arr,0,len(arr)-1)

arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
d = int(input("Enter the number of positions to rotate the array: "))
sol = Solution()
sol.rotateArr(arr, d)
print("Rotated array:", arr)