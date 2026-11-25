import os
import sys

SCENE = "Dad asked the robot to fix the Wi-Fi; the robot asked Dad to fix his password. They have been troubleshooting each other for an hour, and somehow the whole house feels closer for it."


def main():
    os.makedirs("/output", exist_ok=True)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as out:
            out.write(SCENE)
    except OSError as err:
        sys.exit(f"cannot write entry: {err}")


if __name__ == "__main__":
    main()
