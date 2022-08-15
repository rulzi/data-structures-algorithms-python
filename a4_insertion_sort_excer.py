def insertion_sort(elements):
    print(elements[0])
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor
        if (i+1)%2==1:
            med = elements[(i)//2]
        else:
            x1 = (i+1)//2
            x2 = ((i+1)//2)-1
            med = (elements[x1]+elements[x2])/2
        print(med)

if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5]
    
    insertion_sort(elements)
    print(f'sorted array: {elements}')