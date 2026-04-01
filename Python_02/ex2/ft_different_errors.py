#!/usr/bin/env python3

def not_valid_value(user_number: int) -> int | None:
    """Check that the value is a valid number."""
    try:
        number: int = int(user_number)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        return None

    if number < 0:
        print("Too cold!")
        return None
    elif number > 40:
        print("Too hot!")
        return None
    else:
        print("Valid temperature!")
        return number


def safe_division(first_number: float, second_number: float) -> float | None:
    """Verify that we are not multiplying by 0 (it is not possible)."""
    try:
        number: float = first_number / second_number
        return number
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        return None


def find_file(user_file: str) -> str | None:
    """Check that the file exists and catch the error."""
    try:
        file = open(user_file)
        content: str = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print("Caught FileNotFoundError:"
              f" No such file or directory: '{user_file}'")
        return None


def key_not_found(value: str) -> str | None:
    """Check that the key we need exists within a dictionary, list, etc."""
    try:
        dic: dict[str, str] = {"plant": "tomato"}
        return dic[value]
    except KeyError:
        print(f"Caught KeyError: '{value}'")
        return None


def type_error(value: object) -> None:
    """Test the Type Error."""
    try:
        example = "Hello" + 5
        print(example)
    except TypeError:
        print("Caught TypeError: can only concatenate str (not 'int') to str")


def multiple_errors(value: str) -> None:
    """Test the errors we used previously together."""
    try:
        number: int = int(value)
        number / 0
        open("missing.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")


def garden_operations(operation_number: int) -> None:
    """Trigger a specific faulty operation based on the number."""

    if operation_number == 0:
        not_valid_value("abc")
    elif operation_number == 1:
        safe_division(10, 0)
    elif operation_number == 2:
        find_file("missing.txt")
    elif operation_number == 3:
        type_error(None)
    elif operation_number == 4:
        key_not_found("missing_key")
    elif operation_number == 5:
        multiple_errors("abc")
    else:
        print("No avalaible operation for this number.")


def test_error_types() -> None:
    """Print the script showing all the errors."""
    print("=== Garden Error Types Demo ===")

    for i in range(6):
        print(f"\nTesting operation {i}...")
        garden_operations(i)

    print("\nAll error types tested successfully!")
