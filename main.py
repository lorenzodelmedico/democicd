import sys

from src.democicd.cli import confirm_exit

if __name__ == "__main__":
    if confirm_exit():
        print("Exiting now.")
        sys.exit(0)
    else:
        print("Continuing execution.")
