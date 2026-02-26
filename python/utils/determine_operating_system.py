import os
import platform

def get_system_info():
    os_name = os.name
    os_release = platform.release() if os_name == 'posix' else platform.win32_ver()[0]

    if os_name == 'nt':
        os_name = 'Windows'
    elif os_name == 'posix':
        os_name = 'Unix-like'

    return {
        'Operating System': os_name,
        'Release Version': os_release,
    }

def main():
    # Call the function and assign the returned dictionary to system_info
    system_info = get_system_info()

    # Access individual variables from the system_info dictionary
    os_name = system_info['Operating System']
    os_release = system_info['Release Version']

    # Print the individual variables
    print("Operating System:", os_name)
    print("Release Version:", os_release)

if __name__ == '__main__':
    main()
