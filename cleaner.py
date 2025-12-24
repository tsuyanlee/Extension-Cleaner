import os
import glob
import argparse
import logging
from typing import List


# --------------------------------------------
# Logging Setup
# --------------------------------------------
logging.basicConfig(
    filename="cleanup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
logging.getLogger().addHandler(console)

# --------------------------------------------
# Progress Bar
# --------------------------------------------
def progress_bar(current, total, bar_length=40):
    percent = current / total
    filled = int(bar_length * percent)
    bar = "█" * filled + "-" * (bar_length - filled)
    print(f"\r[{bar}] {percent*100:.1f}%", end="", flush=True)

# --------------------------------------------
# File Finding Function
# --------------------------------------------
def find_files(folder: str, extension: str, recursive: bool) -> List[str]:
    pattern = f"**/*{extension}" if recursive else f"*{extension}"
    full_pattern = os.path.join(folder, pattern)

    try:
        files = glob.glob(full_pattern, recursive=recursive)
        logging.info(f"Found {len(files)} file(s) with extension {extension}")
        return files
    except Exception as e:
        logging.error(f"Error scanning folder: {e}")
        return []

# --------------------------------------------
# Delete Files Function With Progress Bar
# --------------------------------------------
def delete_files(files: List[str]):
    total = len(files)

    # Turn off logging to console during progress bar
    console.setLevel(logging.CRITICAL)

    for i, file_path in enumerate(files, start=1):
        try:
            os.remove(file_path)
            logging.info(f"Deleted: {file_path}")  # still logs to file
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
        except PermissionError:
            logging.error(f"Permission denied: {file_path}")
        except Exception as e:
            logging.error(f"Error deleting {file_path}: {e}")

        # Update progress
        progress_bar(i, total)

    # Restore console logging
    console.setLevel(logging.INFO)

    print()  # move to next line


# --------------------------------------------
# Main CLI Entry
# --------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Delete files by extension with optional recursion and progress bar."
    )

    parser.add_argument("folder", help="Folder to search")
    parser.add_argument("extension", help="Extension to delete (e.g. .txt)")
    parser.add_argument("-r", "--recursive", action="store_true", help="Delete recursively")
    parser.add_argument("--dry", action="store_true", help="List files without deleting")

    args = parser.parse_args()

    folder = args.folder
    extension = args.extension

    if not os.path.isdir(folder):
        logging.error("Invalid folder path.")
        print(" Folder not found.")
        return

    # Find files
    files = find_files(folder, extension, args.recursive)

    if not files:
        print("No matching files found.")
        return

    print(f"Found {len(files)} file(s):")
    for f in files:
        print(" -", f)

    if args.dry:
        print("\n(dry run: no files deleted)")
        return

    print("\nDeleting files...\n")
    delete_files(files)

    print("\n✔ Cleanup complete! Check cleanup.log for details.")

if __name__ == "__main__":
    main()
