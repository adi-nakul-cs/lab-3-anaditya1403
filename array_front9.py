# Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
# The array length may be less than 4.


# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
  for i in range(len(nums) - 4):
    if nums[i] == 9 or nums[i + 1] == 9 or nums[i + 2] == 9 or nums[i + 3] == 9:
      return True
      
  else:
    return False
    
if __name__ == "__main__":
  print(array_front9([4,8,9,9,8]))

#Code not yet Completed/...