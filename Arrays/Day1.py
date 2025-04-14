class Solution:
    #This is one program where the T.C is O(n)
    def getSecondLargest(self, arr):
        first_max = -1
        second_max=first_max
        for i in range(len(arr)):
            curr_ele=arr[i]
            if(curr_ele>second_max and curr_ele>first_max):
                second_max=first_max
                first_max=curr_ele
            elif(curr_ele>second_max and curr_ele<first_max):
                second_max=curr_ele
        if(first_max==second_max):
            return first_max
        else:
            return second_max
        
if __name__ == "__main__":
    input_str = input("Enter numbers separated by spaces: ")
    input_list = list(map(int, input_str.strip().split()))
    
    solution = Solution()
    result = solution.getSecondLargest(input_list) 
 