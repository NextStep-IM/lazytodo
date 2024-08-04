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
    

if __name__ == "__main__":
    main()