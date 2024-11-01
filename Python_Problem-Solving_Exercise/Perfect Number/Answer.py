# Determine all the perfect numbers from the given range.

def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num


def perfect_number_in_range(start, end):
    perfect_num = []
    for num in range(start, end + 1):
        if perfect_number(num):
            perfect_num.append(num)
    return perfect_num


start = int(input())
end = int(input())

isPerfect_number = perfect_number_in_range(start, end)
print("Perfect numbers in given range", isPerfect_number)
