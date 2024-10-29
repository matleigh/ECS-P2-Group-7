# Hang Yu Chen decode function

import pandas as pd

# Load the Excel data to create the dictionary
xl = pd.read_excel("P2M012_G7.xlsx")
bins = list(xl["Bins"])
chars = list(xl["Chars"])

# Create the dictionary to map binary codes to characters
compareDict = {}
for key in bins:
    for string in chars:
        # Handle newline characters
        if string == "\\n":
            string = "\n"
        compareDict[key] = string
        chars.remove(string)
        break


def decode(fn="BinOutput.txt"):
    # Open the file and read the binary data
    with open(fn, 'r') as file:
        data = file.read()

    # Remove any "D." markers from the data
    cleaned_data = data.replace("D.", "")

    decoded_text = ""  # Initialize an empty string to store decoded characters
    i = 0

    # Loop through the binary data, decoding each binary code
    while i < len(cleaned_data):
        # Determine the binary code length based on the first bit
        if cleaned_data[i] == '0':  # Assume '0' indicates a 6-bit character
            binary_code = cleaned_data[i:i + 6]
            i += 6
        else:  # Assume otherwise it's a 4-bit character
            binary_code = cleaned_data[i:i + 4]
            i += 4

        # Use compareDict to find the corresponding character
        character = compareDict.get(binary_code, '?')  # '?' for unknown codes
        decoded_text += character

    # Write the decoded text to the output file
    with open("TextOutput.txt", 'w') as output_file:
        output_file.write(decoded_text)
