import random

def generate_numbers():
    numbers = [random.randint(1, 100) for _ in range(10)]
    print("Generated numbers: ", numbers)
    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    nums = generate_numbers()
    print(f"Sum: {calculate_sum(nums)}")
    print(f"Average: {calculate_average(nums)}")
