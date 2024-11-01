"""Given the participants score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up."""

number = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for i in range(number):
    if arr[i] > arr[i + 1]:
        print(arr[i + 1])
        break
