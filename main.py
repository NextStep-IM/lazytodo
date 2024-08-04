from pathlib import Path
from platform import system
import sys

# Constants
# TODO: Check if these costants can be set only at first run
HOME = Path.home()
OS = system()
FILE_DIR_NAME = "lazytodo"
FILE_NAME = "data.txt"
WINDOWS_LOC = HOME / "AppData" / "Local"
LINUX_LOC = HOME / ".local" / "share"
if OS == "Windows":
    DATA_FILE = WINDOWS_LOC / FILE_DIR_NAME / FILE_NAME
    FILE_DIR = WINDOWS_LOC / FILE_DIR_NAME
elif OS == "Linux":
    DATA_FILE = LINUX_LOC / FILE_DIR_NAME / FILE_NAME
    FILE_DIR = LINUX_LOC / FILE_DIR_NAME
else:
    sys.exit(f"{OS} is not supported. Exiting program.")


def main():
    if not DATA_FILE.exists():
        try:
            Path.mkdir(FILE_DIR, parents=True)  # Creates FILE_DIR and missing parents
        except FileExistsError:
            pass
        print(
            "Welcome to lazytodo!\nPlease enter directory paths (separated by space and inside quotations) which will be searched (e.g, /opt/example_dir or C:\\Users\\Documents\\):\n"
        )
        writeToDataFile()

# Write target Dirs to DATA_FILE
def writeToDataFile():
    Dirs = input("Paths: ").strip().split()
    with open(DATA_FILE, "a") as f:
        for dir in Dirs:
    for dir in Dirs:
        if dir.exists():
            f.write(f"{dir}\n")
        else:
            print(f"\"{dir}\" does not exist. Skipping.")


def menu():
    print("1- Display todo list")
    print("2- Add directories")
    print("3- Exit")
    while True:
        try:
            choice = int(input("Enter (1/2): ").strip())
        except ValueError:
            continue
        else:
            break
    return choice


if __name__ == "__main__":
    main()
