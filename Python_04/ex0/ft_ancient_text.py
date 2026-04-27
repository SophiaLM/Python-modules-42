#!/usr/bin/env python3
import sys


def recovery_system(file_name: str) -> None:
    f = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        content = f.read()
        print(content)

    except FileNotFoundError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 2] No such file or directory: '{file_name}'")
    except PermissionError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 13] Permission denied: '{file_name}'")
    except Exception as error:
        print(f"RESPONSE: Unexpected system anomaly - {error}")
    finally:
        if f is not None:
            f.close()
            print(f"---\nFile '{file_name}' closed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        file_name = sys.argv[1]

        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file_name}'"
              "\n---")

        recovery_system(file_name)
