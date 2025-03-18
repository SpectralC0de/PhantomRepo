def complex_calculation(x, y):
    result = x * y
    return result

def process_data(data):
    processed = [d * 2 for d in data]
    return processed

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(f"Original data: {data}")
    processed_data = process_data(data)
    print(f"Processed data: {processed_data}")
    result = complex_calculation(10, 5)
    print(f"Calculation result: {result}")
