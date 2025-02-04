"""
Main module for the democicd package.

This module provides the entry point for the application.
"""

import sys

from democicd.cli import confirm_exit


def main():
    if confirm_exit():
        print("Exiting now.")
        sys.exit(0)
    else:
        print("Continuing execution.")


if __name__ == "__main__":
    main()
