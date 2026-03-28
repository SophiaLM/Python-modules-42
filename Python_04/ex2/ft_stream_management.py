#!/usr/bin/env python3
import sys


def stream_manager():
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    arch_id = sys.stdin.readline().strip()

    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status = sys.stdin.readline().strip()

    sys.stdout.write(f"[STANDARD] Archive status from {arch_id}: {status}\n")

    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    stream_manager()
