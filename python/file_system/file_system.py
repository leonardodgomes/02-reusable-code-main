"""
file_system.py
Utility functions for interacting with the file system.

Includes:
- get_path(): returns full path, folder, and file name of the script
- bulk_rename_files(): rename multiple files using prefix/suffix/full_name
- rename_file(): rename a single file
- replace_in_filenames(): replace text inside filenames
- change_extension(): change file extensions in a folder
- add_timestamp_to_files(): append timestamps to filenames
- sanitize_filename(): remove illegal characters
"""

import os
import datetime
import re


def get_path():
    full_path = os.path.abspath(__file__)
    folder_path = os.path.dirname(full_path)
    file_name = os.path.basename(full_path)

    return {
        "Full Path": full_path,
        "Folder Path": folder_path,
        "File Name": file_name
    }


def bulk_rename_files(folder_path, rename_option, new_value):
    files = os.listdir(folder_path)
    file_count = 0

    for index, file_name in enumerate(files):
        current_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(current_path):
            continue

        name, ext = os.path.splitext(file_name)

        if rename_option == "full_name":
            new_name = f"{new_value}_{index + 1}{ext}"
        elif rename_option == "prefix":
            new_name = f"{new_value}{file_name}"
        elif rename_option == "suffix":
            new_name = f"{name}{new_value}{ext}"
        else:
            print("Invalid rename option. Choose: full_name, prefix, suffix.")
            return

        os.rename(current_path, os.path.join(folder_path, new_name))
        file_count += 1

    print("Files modified:", file_count)


def rename_file(old_path, new_name):
    folder = os.path.dirname(old_path)
    _, ext = os.path.splitext(old_path)
    new_path = os.path.join(folder, new_name + ext)
    os.rename(old_path, new_path)
    return new_path


def replace_in_filenames(folder_path, old_text, new_text):
    count = 0
    for file_name in os.listdir(folder_path):
        old_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(old_path):
            continue

        new_name = file_name.replace(old_text, new_text)
        os.rename(old_path, os.path.join(folder_path, new_name))
        count += 1

    print("Files renamed:", count)


def change_extension(folder_path, old_ext, new_ext):
    count = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith(old_ext):
            base = file_name[:-len(old_ext)]
            new_name = base + new_ext
            os.rename(
                os.path.join(folder_path, file_name),
                os.path.join(folder_path, new_name)
            )
            count += 1

    print("Extensions changed:", count)


def add_timestamp_to_files(folder_path, position="suffix"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    count = 0

    for file_name in os.listdir(folder_path):
        old_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(old_path):
            continue

        name, ext = os.path.splitext(file_name)

        if position == "prefix":
            new_name = f"{timestamp}_{name}{ext}"
        else:
            new_name = f"{name}_{timestamp}{ext}"

        os.rename(old_path, os.path.join(folder_path, new_name))
        count += 1

    print("Timestamps added:", count)


def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', "", filename)
