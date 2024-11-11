def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = list(map(int, input("Enter numbers: ").split()))

bubbleSort(data)

print("Sorted array:", data)
print("Sum of Largest and Smallest Number:", data[0] + data[-1])
