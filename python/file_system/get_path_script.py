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


def main():
    #Call the function to get the path to the script
    path_complete = get_path()
    
    # Access individual variables from the system_info dictionary
    full_path = path_complete['Full Path']
    folder_path = path_complete['Folder Path']
    file_name = path_complete['File Name']    

    # Print the individual variables
    print('Full Path: ', full_path)
    print('Folder Path: ', folder_path)
    print('File Name:', file_name)


if __name__ == '__main__':
    main()
