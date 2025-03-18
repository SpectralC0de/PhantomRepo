import os

def fake_function():
    return "This function does nothing."

def suspicious_code():
    # Placeholder for 'important' data
    secret_key = "hidden_key_12345"
    print("This function should never be called.")
    return secret_key

def broken_code():
    print("Trying to open a file that doesn't exist...")
    open("non_existent_file.txt", "r")

if __name__ == "__main__":
    print(fake_function())
    suspicious_code()  # This should never be executed in production!
    broken_code()
