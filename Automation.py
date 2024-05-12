import os
import shutil

def organize_files(source, destination):
    
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    
    files = os.listdir(source)
    
    
    for file in files:
        
        file_path = os.path.join(source, file)
        
        
        if os.path.isfile(file_path):
            
            _, extension = os.path.splitext(file)
            
            
            extension = os.path.join(destination, extension[1:])
            if not os.path.exists(extension):
                os.makedirs(extension)
            
            
            shutil.move(file_path, os.path.join(extension, file))
            print(f"Moved {file} to {destination}")


source_directory = "F:\\CodeAlpha\\Task 4"
destination_directory = "F:\\CodeAlpha\\Task 4"

organize_files(source_directory, destination_directory)
print("All files has been automated")
