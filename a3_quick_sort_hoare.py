def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    
    start = pivot_index + 1
    
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
            
        while elements[end] > pivot:
            end -= 1
        
        if start < end:
            swap(start, end, elements)
        
    swap(pivot_index, end, elements)
    
    return end
        
def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        # left
        quick_sort(elements, start, pi-1)
        # right
        quick_sort(elements, pi+1, end)

if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    
    quick_sort(elements, 0, len(elements)-1)
    print(elements)