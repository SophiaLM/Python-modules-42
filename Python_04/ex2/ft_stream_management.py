#!/usr/bin/env python3
import sys


def preservation_system(file_name: str) -> None:
    f = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        content = f.read()

        sys.stdout.write("---\n")
        sys.stdout.write(content + "\n")
        sys.stdout.write("---\n")

        f.close()
        sys.stdout.write(f"File '{file_name}' closed.\n\n")
        f = None

        sys.stdout.write("Transform data:\n---\n")

        lines = content.splitlines()
        new_content = ""

        for line in lines:
            transformed_line = line + "#"
            sys.stdout.write(transformed_line + "\n")
            new_content += transformed_line + "\n"

        sys.stdout.write("---\n")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        save_name = sys.stdin.readline().strip()

        if save_name != "":
            sys.stdout.write(f"Saving data to '{save_name}'\n")
            out_f = open(save_name, "w", encoding="utf-8")
            out_f.write(new_content)
            out_f.close()
            sys.stdout.write(f"Data saved in file '{save_name}'.\n")
        else:
            sys.stdout.write("Not saving data.\n")

    except FileNotFoundError:
        sys.stderr.write(
            f"[STDERR] Error opening file '{file_name}': "
            f"[Errno 2] No such file or directory: '{file_name}'\n"
        )
    except PermissionError:
        sys.stderr.write(
            f"[STDERR] Error opening file '{file_name}': "
            f"[Errno 13] Permission denied: '{file_name}'\n"
        )
    except Exception as error:
        sys.stderr.write(f"[STDERR] Unexpected system anomaly - {error}\n")

    finally:
        if f is not None:
            f.close()
            sys.stdout.write(f"---\nFile '{file_name}' closed.\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stdout.write(f"Usage: {sys.argv[0]} <filename>\n")
    else:
        arg_file = sys.argv[1]
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
        sys.stdout.write(f"Accessing file '{arg_file}'\n")
        preservation_system(arg_file)
