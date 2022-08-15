def bubble_sort(elements):
    size = len(elements)
    
    for k in range(size-1):
        swapped = False
        for i in range(size-1-k):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped = True
        if not swapped:
            break
            
    return elements 
    

if __name__ == "__main__":
    elements = [5,9,2,1,67,34,88,34]
    
    sort = bubble_sort(elements)
    print(sort)