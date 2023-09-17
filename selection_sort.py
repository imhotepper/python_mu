print('Selection sort:');

def smallest_in_list(list):
    smallest_index= 0
    smallest_item = list[0]
    for i in range(0, len(list)):
        if list[i] < smallest_item:
            smallest_item = list[i]
            smallest_index =  i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        idx = smallest_in_list(arr)
        new_arr.append( arr.pop(idx))
    return new_arr


print(selection_sort([-1,2, -7,3, -12, 0, -99]))
print(selection_sort([7,5,4]))
print(selection_sort([1000, -400, 0, 22]))