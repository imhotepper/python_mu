print('Selection sort:');

def smallesInList(list):
    smallest_index= 0
    smallest_item = list[0]
    for i in range(0, len(list)):
        if list[i] < smallest_item:
            smallest_item = list[i]
            smallest_index =  i
    return smallest_index


def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        idx = smallesInList(arr)
        new_arr.append( arr.pop(idx))
    return new_arr


print(selectionSort([-1,2, -7,3, -12, 0, -99]))
print(selectionSort([7,5,4]))
print(selectionSort([1000, -400, 0, 22]))


