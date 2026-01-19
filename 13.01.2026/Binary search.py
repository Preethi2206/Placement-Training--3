arr = list(map(int, input().split()))
key = int(input())

low, high = 0, len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

print("Found" if found else "Not Found")
