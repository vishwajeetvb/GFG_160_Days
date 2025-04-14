## Here the T.C is O(N)
# here the logic is that if the num will be at its highest permutation then all the digits will be sorted in desc order
# if not, then till the place the digits are sorted in desc, and whenever ther's break in pattern which means from there the
# next permutation will be made. For ex if its  [3 2 1] then its at highest permutation
# if its at [534976] here if you see 6<7<9 but 9>4 so here the pattern is breaking which means whatever next digit is greater then
# 4 will make the next permuattion so num > 4 is 6 as its sroted in desc so if we traverse from right we will find the next greater 
# number then 4, then just swap it and then reverse the array after that num for example here swap 4<->6 and then swap 974
#So final result will be [534976] = [536479]

class Solution:
    
    def rev(self,arr,start,end):
        while(start<end):
            temp = arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1
    def nextPermutation(self, arr):
        index=-1
        for i in range(len(arr)-1,0,-1):
            if(arr[i]>arr[i-1]):
                index=i-1
                break
        for i in range(len(arr)-1,index,-1):
            if(arr[i]>arr[index]):
                temp=arr[i]
                arr[i]=arr[index]
                arr[index]=temp
                break
        if index!=-1:
            self.rev(arr,index+1,len(arr)-1)
        else:
            arr.sort()

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
sol = Solution()
sol.nextPermutation(arr)
print("Next permutation:", arr)