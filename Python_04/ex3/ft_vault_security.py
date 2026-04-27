#!/usr/bin/env python3


def secure_archive(file_name: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r", encoding="utf-8") as f:
                data = f.read()
            return (True, data)

        elif action == "write":
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(content)
            return (True, "Content successfully written to file")

        return (False, f"Invalid action: {action}")

    except FileNotFoundError:
        return (False, f"[Errno 2] No such file or directory: '{file_name}'")
    except PermissionError:
        return (False, f"[Errno 13] Permission denied: '{file_name}'")
    except Exception as e:
        return (False, f"Unexpected system anomaly - {e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    success, content_data = secure_archive("ancient_fragment.txt", "read")
    print((success, content_data))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive("new_archive.txt", "write", content_data))
    else:
        print(secure_archive("new_archive.txt", "write", "No data found."))
