some_bytes = b'\xC3\xA9'
 
# Open in "wb" mode to
# write a new file, or
# "ab" mode to append
with open("my_file1.txt", "wb") as binary_file:
   
    # Write bytes to file
    binary_file.write(some_bytes)