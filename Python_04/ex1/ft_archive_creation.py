#!/usr/bin/env python3
import sys


def preservation_system(file_name: str) -> None:
    try:
        f = open(file_name, "r", encoding="utf-8")
        content = f.read()

        print("---")
        print(content)
        print("---")

        print("Transform data:")
        print("---")

        lines = content.splitlines()
        new_content = ""

        for line in lines:
            transformed_line = line + "#"
            print(transformed_line)
            new_content += transformed_line + "\n"

        print("---")
        save_name = input("Enter new file name (or empty): ")

        if save_name != "":
            print(f"Saving data to '{save_name}'")
            out_file = open(save_name, "w", encoding="utf-8")
            out_file.write(new_content)
            out_file.close()
            print(f"Data saved in file '{save_name}'.")
        else:
            print("Not saving data.")

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
        print(f"Usage: {sys.argv[0]} <filename>")
    else:
        arg_file = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{arg_file}'")

        try:
            preservation_system(arg_file)
        except Exception as e:
            print(f"Error opening file '{arg_file}': {e}")
