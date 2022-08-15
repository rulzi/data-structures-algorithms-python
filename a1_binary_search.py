def binary_search(numbers, number_to_find):
    left_index = 0
    right_index = len(numbers)-1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_number = numbers[mid_index]
        
        if number_to_find == mid_number:
            return mid_index
        
        if number_to_find > mid_number:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
            
    return -1

def binary_search_recursive(numbers, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index)//2
    mid_number = numbers[mid_index]
    
    if mid_number == number_to_find:
        return mid_index
    
    if number_to_find > mid_number:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
            
    return binary_search_recursive(numbers, number_to_find, left_index, right_index)

if __name__ == "__main__":
    numbers = [2,9,10,20,50,88,78,94]
    number_to_find = 23123
    
    # print(binary_search(numbers, number_to_find))
    print(binary_search_recursive(numbers, number_to_find, 0, len(numbers)-1))