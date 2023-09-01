import random

# Создаем массив рандомных данных
array_size = 10
random_data = [random.randint(1, 100) for _ in range(array_size)]
print("Исходный массив:")
print(random_data)

# Bubble Sort (Сортировка пузырьком)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sorted = random_data.copy()
bubble_sort(bubble_sorted)
print("Сортировка пузырьком:")
print(bubble_sorted)

# Selection Sort (Сортировка выбором)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sorted = random_data.copy()
selection_sort(selection_sorted)
print("Сортировка выбором:")
print(selection_sorted)

# Insertion Sort (Сортировка вставками)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

insertion_sorted = random_data.copy()
insertion_sort(insertion_sorted)
print("Сортировка вставками:")
print(insertion_sorted)

# Merge Sort (Сортировка слиянием)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

merge_sorted = random_data.copy()
merge_sort(merge_sorted)
print("Сортировка слиянием:")
print(merge_sorted)
