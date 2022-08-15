def selection_sort(arr):
    for i in range(len(arr) -1):
        compare_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[compare_index]:
                compare_index = j
        if i != compare_index:
            arr[i], arr[compare_index] = arr[compare_index], arr[i]

if __name__ == "__main__":
    elements = [21,38,29,17,4,25,11,31,9]
    selection_sort(elements)
    print(elements)