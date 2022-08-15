from pyrsistent import s


def selection_sort(arr, sort_by_list):
    for i in range(len(arr) -1):
        compare_index = i
        for j in range(i+1, len(arr)):
            for sort_by in sort_by_list:
                if arr[j][sort_by] < arr[compare_index][sort_by]:
                    compare_index = j
                    break
                if arr[j][sort_by] > arr[compare_index][sort_by]:
                    break
        if i != compare_index:
            arr[i], arr[compare_index] = arr[compare_index], arr[i]

if __name__ == "__main__":
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    
    selection_sort(elements, ["First Name", "Last Name"])
    print(elements)