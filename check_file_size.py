import os
import sys
import shutil

def find_and_copy_large_files(size_threshold_mb):


    #get the current directory
    current_path = os.path.abspath(sys.argv[0])
    root_directory = os.path.dirname(current_path) # the directory we begin the search from

    target_folder = os.path.join(root_directory, 'large_files') #creates a folder in the root directory to add the large folders 
    output_file_path= os.path.join(target_folder, 'large_files.txt') # creates the .txt file that contains the path to the size exceeding files

    
    #size of file converted to bytes
    size_threshold_bytes = size_threshold_mb * 1024 * 1024
    large_files = []

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for root, dirs, files in os.walk(root_directory):

        #we need to skip the target_folder when searching
        dirs[:] = [d for d in dirs if os.path.join(root, d) != target_folder]

        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path) #size of file in bytes
                if file_size > size_threshold_bytes:
                    large_files.append(file_path) #save the path in the list
                    shutil.copy2(file_path, target_folder) #copy the file in the target_folder directory
    
    #write the file paths to a .txt file
    with open(output_file_path, 'w') as f:
        for file_path in large_files:
            f.write(file_path + '\n')

    print(f"The paths of files larger {output_file_path}")
    print(f"The files have been copied to {target_folder}")


def main():
    try:
        the_input = input("Enter the size of the files in MB:")
        megabytes = float(the_input)
    except ValueError:
        print(f"Cannot convert '{the_input}' to a number.")
    find_and_copy_large_files(megabytes)

main()