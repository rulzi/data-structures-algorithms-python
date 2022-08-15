def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements, start, end):
    pivot = elements[end]
    temp_index = start
    
    for i in range (start, end):
        if elements[i] <= pivot:
            swap(temp_index, i, elements)
            temp_index += 1
            
    swap(temp_index, end, elements)
    
    return temp_index
        
def quick_sort(elements, start, end):
    if start >= end or start < 0:
        return
    
    pi = partition(elements, start, end)
    
    # left
    quick_sort(elements, start, pi-1)
    # right
    quick_sort(elements, pi+1, end)

if __name__ == "__main__":
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    
    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')