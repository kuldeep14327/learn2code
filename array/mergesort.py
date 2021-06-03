#mergesort function
def mergesort(array):
    if len(array) > 1:
        mid = len(array)//2
        left_array = array[:mid] ## divide the array into 2 parts left $ right
        right_array = array[mid:]
        print(left_array, right_array)
        mergesort(left_array)
        mergesort(right_array)
        

        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
                k += 1
            else:
                array[k] = right_array[j]
                j += 1
                k += 1
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
    return array

size = int(input("specify the array size:"))
myarr = [int(input()) for i in range(size)]
print("Input array is: ", myarr)
# mergesort(myarr)
print("sorted array is: ", mergesort(myarr))