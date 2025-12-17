import os
import glob
import logging
import time

# --------------------------------------------
# Logging Setup
# --------------------------------------------
logging.basicConfig(
    filename="cleanup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_files(folder: str, extension: str, recursive: bool = True):
    pattern = "**/*" + extension if recursive else "*" + extension
    search_path = os.path.join(folder, pattern)

    try:
        return glob.glob(search_path, recursive=recursive)
    except Exception as e:
        logging.error(f"Error finding files: {e}")
        return []


def progress_bar(current, total, bar_length=40):
    """Draw a simple progress bar."""
    percent = (current / total)
    filled = int(bar_length * percent)
    bar = "█" * filled + "-" * (bar_length - filled)
    print(f"\r[{bar}] {percent*100:.1f}%", end="", flush=True)


def delete_files(folder: str, extension: str, recursive: bool = True):
    files = find_files(folder, extension, recursive)

    if not files:
        print("No files found.")
        return

    total = len(files)
    print(f"Found {total} file(s).\n")

    for i, file_path in enumerate(files, start=1):
        try:
            os.remove(file_path)
            logging.info(f"Deleted: {file_path}")
        except Exception as e:
            logging.error(f"Error deleting {file_path}: {e}")

        # Update progress bar
        progress_bar(i, total)
        time.sleep(0.05)  # small delay so bar is visible (optional)

    print("\n\nDeletion complete!")


# Example usage
if __name__ == "__main__":
    folder = input("Enter the name of the folder: ")
    extension = input("Enter the extension: ")
    delete_files(folder, extension)
