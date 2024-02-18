n = int(input("Enter a sequence number:  "))

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence

# Example usage
print(fibonacci(n))
