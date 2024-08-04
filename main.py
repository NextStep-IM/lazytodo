from pathlib import Path
from platform import platform
import sys

# Constants
# TODO: Check if these costants can be set only at first run
HOME = Path.home()
OS = platform()
FILE_NAME = "data.txt"
if OS == "Windows":
    DATA_FILE = HOME / "AppData" / "Local" / "lazytodo" / FILE_NAME
elif OS == "Linux":
    DATA_FILE = HOME / ".local" / "share" / "lazytodo" / FILE_NAME
else:
    sys.exit(f"{OS} is not supported. Exiting program.")


def main():
    if not DATA_FILE.exists():
        print(
            "Welcome to lazytodo!\nPlease enter directory paths (separated by space) which will be searched:\n"
        )
        writeToDataFile()

def writeToDataFile():
    Dirs = input("Paths: ").strip().split()
    with open(DATA_FILE, "a") as f:
        for dir in Dirs:
            f.write(f"{dir}\n")


if __name__ == "__main__":
    main()