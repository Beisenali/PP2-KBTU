def unique_elements(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
