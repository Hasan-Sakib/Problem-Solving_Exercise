def armstrong(num):
    len1 = len(str(num))

    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** len1
        temp //= 10
    return num == sum


num = int(input('Enter your number: '))

if armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")