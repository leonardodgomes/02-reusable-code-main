
# importing os module
import os
 
# Function to rename multiple files
def main():
   
    folder = "PUT_THE_PATH_HERE"
    for count, file in enumerate(os.listdir(folder)):
        filename, extension = os.path.splitext(file)
        dst =f"{filename}NEW_TEXT{extension}"
        src =f"{folder}/{file}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()