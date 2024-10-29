"""
Yavuz Yildiz
Explanation: This function reads a text file, converts the ‘characters’ to
binary codes, and writes those codes into a text file.
"""

# Global variables that store binary codes and characters
bin_codes = []
chars = []


# Encoding the text file
def encode(fn):
    bin_output = ""  # Starts with empty string

    with open(fn, 'r') as file:  # Opens the file for reading
        text = file.read()

    i = 7  # Initialize index for iterating through text

    while i < len(text):    # Iterate through the text
        match_found = False

        # Check for matches in chars with different substring lengths
        for char in chars:
            if text[i:i + len(char)] == char:
                # Finds the index of the multicharacter match
                index = chars.index(char)

                # Uses index to find the matching binary code
                bin_output += bin_codes[index]

                # Move index forward by length of matched string
                i += len(char)
                match_found = True
                break  # Exit the loop once a match is found

        # If no match is found, move to the next character
        if not match_found:
            i -= 1

    total_bits = len(bin_output)  # Total number of bits used

    # Write to BinOutput.txt
    with open('BinOutput.txt', 'w') as file:  # Used to write the file
        file.write(f"{total_bits}.{bin_output}")
