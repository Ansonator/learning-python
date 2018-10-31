original = [1,2,3,4,5,6,7,8,9,10]


def find_index_of_largest(numbers):
    largest_index = 0
    largest = numbers[largest_index]
    for i in range(1,len(numbers)):
        if (numbers[i] > largest):
            largest = numbers[i]
            largest_index = i
    return (largest_index)

def all_equal(numbers):
    first = numbers[0]
    for i in range(1,len(numbers)):
        if (numbers[i] != first):
            return False
    return True

def increment_to_largest(current, original):
    largest_index = find_index_of_largest(current)
    largest_number = current[largest_index]
    for i in range(0, len(current)):
        if (i != largest_index):
            while (current[i] < largest_number):
                current[i] += original[i]
    return (current)

current = original.copy()
while (not all_equal(current)):
    current = increment_to_largest(current, original)
    
print("The LCM of",original,"is",current[0])