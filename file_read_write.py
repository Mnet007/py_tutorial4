def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the entire content of the file
        
        # Modify the content (for example, converting it to uppercase)
        modified_content = content.upper()  # You can modify this logic as needed
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been successfully modified and written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ask the user for the filename and the new filename
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the file to write: ")

# Call the function to process the files
read_and_write_file(input_filename, output_filename)
