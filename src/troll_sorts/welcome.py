import time
import sys
import os
from pathlib import Path



def show_welcome(force=False):
    """
    Displays a word animation for TROLLSORTS.
    By default, it only runs once unless force=True.
    """
    welcome_file = Path.home() / ".trollsorts_welcomed"
    if welcome_file.exists() and not force:
        return

    ascii_art = [
        r"  _____ _____   ____  _      _        _____  ____  _____ _______  _____ ",
        r" |_   _|  __ \ / __ \| |    | |      / ____|/ __ \|  __ \__   __|/ ____|",
        r"   | | | |__) | |  | | |    | |     | (___ | |  | | |__) | | |  | (___  ",
        r"   | | |  _  /| |  | | |    | |      \___ \| |  | |  _  /  | |   \___ \ ",
        r"   | | | | \ \| |__| | |____| |____  ____) | |__| | | \ \  | |   ____) |",
        r"   |_| |_|  \_\\____/|______|______||_____/ \____/|_|  \_\ |_|  |_____/ "
    ]

    # Standard reveal animation using plain text
    for line in ascii_art:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write("\n")
    sys.stdout.flush()

    # Mark as welcomed in the user's home directory
    try:
        welcome_file.touch()
    except Exception:
        # If we can't write to the home directory, we just won't save the state
        pass

def main():
    """CLI entry point"""
    show_welcome(force=True)

if __name__ == "__main__":
    main()
