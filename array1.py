def insert_element(arr, pos, value):
    n = len(arr)
    shifts = 0

    
    arr.append(0) 
    for i in range(n, pos, -1):
        arr[i] = arr[i - 1]
        shifts += 1

    arr[pos] = value

    # Complexity
    if pos == n:
        complexity = "O(1)"
    else:
        complexity = "O(n)"

    return arr, shifts, complexity


def delete_element(arr, pos):
    n = len(arr)
    shifts = 0

   
    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]
        shifts += 1

    arr.pop()

    # Complexity
    if pos == n - 1:
        complexity = "O(1)"
    else:
        complexity = "O(n)"

    return arr, shifts, complexity


# ----------- DRIVER CODE -----------

# Input
arr = list(map(int, input("Enter elements: ").split()))
print("Original Array:", arr)

# Insert
pos = int(input("Enter insert position (0-based): "))
value = int(input("Enter value to insert: "))

arr, shifts, complexity = insert_element(arr, pos, value)
print("\nAfter Insertion:", arr)
print("Shift Count:", shifts)
print("Time Complexity:", complexity)

# Delete
pos = int(input("\nEnter delete position (0-based): "))

arr, shifts, complexity = delete_element(arr, pos)
print("\nAfter Deletion:", arr)
print("Shift Count:", shifts)
print("Time Complexity:", complexity)