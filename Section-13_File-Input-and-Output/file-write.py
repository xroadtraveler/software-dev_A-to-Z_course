def write_file(file_path: str, text: str) -> int:
    file = None # handler
    try:
        file = open(file_path, "w")
        return file.write(text)
    except OSError:
        print(f"Error! Couldn't open file at path {file_path}")
    finally:
        if file != None: # checks handler
            file.close()

filename = "myfile.txt"
count = write_file(filename, "Hello Python!") # handler

if count != None: # checks handler
    print(f"{count} characters written to {filename}")
else:
    print(f"Could not write to file{filename}")

import os
print(os.path.abspath(os.getcwd())) # prints our current working directory
