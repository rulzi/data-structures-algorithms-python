# O(1)
from math import ceil


def find_index_number(numbers, index):
    return numbers[index]

# O(n)
def get_square_number(numbers):
    square_numbers = []
    for number in numbers:
        square_numbers.append(number*number)
        
    return square_numbers

# O(n2)
def search_duplicate_number(numbers):
    duplicate_number = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i] == numbers[j]):
                duplicate_number.append(numbers[i])
    
    return duplicate_number

# O(log n)
def search_number(numbers, number):
    total_num = len(numbers)
    half_num = total_num//2
    numbers = sorted(numbers)
    
    if numbers[half_num-1] == number:
        return True
    
    if total_num > 1:
        if numbers[half_num-1] > number:
            return search_number(numbers[0:half_num], number)
        else:
            return search_number(numbers[half_num:total_num], number)
        
    return False

numbers = [2,9,10,20,50,88,78,94]
numbers_dupl = [2,6,10,6,2,8,4]

# print(find_index_number(numbers, 3))
# print(get_square_number(numbers))
# print(search_duplicate_number(numbers_dupl))
# print(search_number(numbers, 50))
