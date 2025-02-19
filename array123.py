# Given an array of ints, return True if the sequence of numbers 1, 2, 3
#  appears in the array somewhere.


# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(num):
    for i in range(len(num) - 2):
        if num[i] == 1 and num[i + 1] == 2 and num[i + 2] == 3:
            return True
        
    else:
        return False
        

if __name__ == "__main__":
    print(array123([4,1,4,3,2,1,2,3,4,5,6]))