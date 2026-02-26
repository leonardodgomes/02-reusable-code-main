import os


def get_path():
    # Get the absolute path of the script
    full_path = os.path.abspath(__file__)
    folder_path = os.path.dirname(full_path)
    file_name = os.path.basename(full_path)


    return {
            'Full Path': full_path,
            'Folder Path': folder_path,
            'File Name': file_name
    }


def list_all_files(folder_path):
    files = []
    count = 0
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            files.append(file)
            count += 1
    return files, count


def list_files_by_folder(folder_path):
    file_paths = []
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
            count += 1
    return file_paths, count


def main():
    #Call the function to get the path to the script
    path_complete = get_path()
    folder_path = path_complete['Folder Path']

    # Call the function and store the result in a variable
    files_root_folder, count_root  = list_all_files(folder_path)

    # Call the function and store the result in a variable
    files_root_subfolders, count_root_subfolders = list_files_by_folder(folder_path)


    # Print the list of file names in the root folder
    for file_name in files_root_folder:
        print(file_name) 
    

    # Print the list of file paths in the root folder and in the subfolders.
    for file_path in files_root_subfolders:
        print(file_path)


    print('Count the number of files in the root folder:', count_root) # Print the file count    
    print('Count the number of files in the root folder and its subfolders:', count_root_subfolders) # Print the file count

if __name__ == '__main__':
    main()
