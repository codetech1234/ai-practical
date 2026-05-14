def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
rules = {
    "small": insertion_sort,
    "medium": selection_sort,
    "large": bubble_sort
}
def choose_sort(arr):
    n = len(arr)
    if n <= 5:
        rule = "small"
    elif n <= 10:
        rule = "medium"
    else:
        rule = "large"
    print("Reasoning: Using", rule, "data rule")
    sorting_function = rules[rule]
    return sorting_function(arr)


data = list(map(int, input("Enter numbers separated by space: ").split()))

sorted_data = choose_sort(data)

print("Sorted List:", sorted_data)