#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int | None:
    """
    Check the temperature and catch the error
    """
    try:
        print(f"\nInput data is: {temp_str}")
        temp = int(temp_str)
    except ValueError:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: {temp_str}")
        return None

    print(f"Temperature is now {temp}°c")
    return (temp)


def test_temperature() -> None:
    """
    Test different temperatures or posibily errors
    """
    print("=== Garden Temperature ===")
    for value in ["25", "abc"]:
        try:
            input_temperature(value)
        except ValueError as error:
            print(error)
    print("\nAll tests completed - program didn't crash!")
