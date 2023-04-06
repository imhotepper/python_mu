print("Binary search:")

def binary_search(arr, item):
    low, high = 0, len(arr) - 1
    while low <= high:
        i = (low + high) // 2
        guess = arr[i]
        if guess == item:
            return item

        if item >= guess:
            low = i + 1
        else:
            high = i - 1
    return None


arr = [1, 2, 45, 77, 85, 98]
find = 45
print(
    f'looking for {find} inside {arr} and I found: { binary_search(arr, find) }')
find = 1
print(
    f'looking for {find} inside {arr} and I found: { binary_search(arr, find) }')
find = 98
print(
    f'looking for {find} inside {arr} and I found: { binary_search(arr, find) }')
find = 450
print(
    f'looking for {find} inside {arr} and I found: { binary_search(arr, find) }')
