import os
import shutil

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not valid")
        return

    items = os.listdir(folder_path)
    files = [f for f in items if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("No files found in directory")
        return

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        _, extension = os.path.splitext(file_name)
        extension = extension[1:].lower() or "no_extension"

        target_dir = os.path.join(folder_path, extension)
        os.makedirs(target_dir, exist_ok=True)


        shutil.move(file_path, os.path.join(target_dir, file_name))
        print(f"Moved: {file_name} -> {extension}/")


organize_folder(folder_path = input("Enter folder path: "))