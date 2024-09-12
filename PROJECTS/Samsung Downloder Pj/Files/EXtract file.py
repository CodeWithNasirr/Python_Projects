import struct

# Define the hex value to search for
samsung_hex_value = b'\x53\x45\x43\x57\x55\x50'

# Open the binary file
with open("P03CFM.bin", "rb") as file:
    # Read the content of the file
    samsung_content = file.read()
    
    # Find the index of the hex value in the content
    samsung_index = samsung_content.find(samsung_hex_value)
    
    # If the hex value is found
    if samsung_index != -1:
        # Adjust the index (assuming 13 bytes offset)
        samsung_index += 13
        
        # Extract the next 3 bytes after the adjusted index
        next_bytes = samsung_content[samsung_index:samsung_index+3]
        
        # Decode the extracted bytes as ASCII
        samsung_id = next_bytes.decode('ascii')
        
        # Print the Samsung ID
        print("Samsung ID:", samsung_id)
