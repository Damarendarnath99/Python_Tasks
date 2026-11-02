import os
import shutil
import sys


def move_jpgs(source_folder, target_name="jpg_images"):
    """Move every .jpg/.jpeg file from source_folder into a new subfolder.

    Returns the number of files moved.
    """
    if not os.path.isdir(source_folder):
        print(f"Error: '{source_folder}' is not a valid folder.")
        return 0

    target_folder = os.path.join(source_folder, target_name)
    moved = 0

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Only look at files (skip folders) with a .jpg / .jpeg extension
        if not os.path.isfile(source_path):
            continue
        if not filename.lower().endswith((".jpg", ".jpeg")):
            continue

        # Create the target folder only when we find the first image
        os.makedirs(target_folder, exist_ok=True)

        destination = os.path.join(target_folder, filename)

        # Avoid overwriting a file with the same name
        if os.path.exists(destination):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination):
                destination = os.path.join(target_folder, f"{base}_{counter}{ext}")
                counter += 1

        shutil.move(source_path, destination)
        print(f"Moved: {filename}")
        moved += 1

    return moved


def main():
    # Use a folder passed on the command line, or ask for one
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Enter the folder path to organize: ").strip()

    count = move_jpgs(folder)

    if count == 0:
        print("No .jpg files were moved.")
    else:
        print(f"\nDone! Moved {count} file(s) into '{os.path.join(folder, 'jpg_images')}'.")


if __name__ == "__main__":
    main()
