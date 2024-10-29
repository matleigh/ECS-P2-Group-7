#Tamar Shuster
##goal is to read in excel file and find binary values and characters using dictionary and lists
import pandas as pd #xxlrd xlrd3 try to install if pandas isn't working
xl = pd.read_excel("P2M012_G7.xlsx")
# sets two global variables (bins and chars) to the values set in
# ^the excel file
bins = list(xl["Bin"]) #sets binary numbers to list as bins
chars = list(xl["Char"]) #sets characters to list as chars

compareDict = {} #empty dictionary: compares pairs from bins and chars lists

chars2 = [] # empty list: initializing the end list
for key in bins:
    for string in chars:
        if string == "\\n": #checks if the value in chars is \\n
            string == ("\n") #sets the value in chars as \n if its \\n
        compareDict[key]= string #sets pairs from both lists as loop iterates
        chars2.append(string) #makes new lists without \\n

        #below removes \\n from the char list
        if string == "\n":
            chars.remove('\\n')
        else:
            chars.remove(string)

        break

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

    i = 0  # Initialize index for iterating through text

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
            i += 1

    total_bits = len(bin_output)  # Total number of bits used

    # Write to BinOutput.txt
    with open('BinOutput.txt', 'w') as file:  # Used to write the file
        file.write(f"{total_bits}.{bin_output}")

# Hang Yu Chen Decode function

'''
import pandas as pd

# Load the Excel data to create the dictionary
xl = pd.read_excel("P2M012_G7.xlsx")
bins = list(xl["Bins"])
chars = list(xl["Chars"])
'''

'''
compareDict = {}
for key in bins:
    for string in chars:
        # Handle newline characters
        if string == "\\n":
            string = "\n"
        compareDict[key] = string
        chars.remove(string)
        break
'''
# Hang Yu Chen
# Create the dictionary to map binary codes to characters
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

# Matilda Leighton

# function that compares two texts files to see if their characters are the same
def same(fn1, fn2="TextOutput.txt"):
    # variables for opening and reading each text file
    fa = open(fn1)
    fb = open(fn2)
    f1 = fa.read()
    f2 = fb.read()
    # if the files are not the same
    if f1 != f2:
        # print that the files are different
        print("Different Files")
        # string variable for the lengths of the files
        lengths = f"file 1: {len(f1)} and file 2: {len(f2)}"
        # create a list that will store the differences between the files
        differences = []
        # iterate through every character in file 1
        for index, char in enumerate(f1):
            # compare each character in file 1 to the one in file 2 with the corresponding index
            if char != f2[index]:
                # if the characters are different, create a string variable of the format "N: C1: C2"
                # N = index, C1 = char in file 1, C2 = char in file 2
                diff = f"{index}: {char}: {f2[index]}"
                # add the variable to the list of differences
                differences.append(diff)
        # create a text file for the errors
        fc = "Errors.txt"
        f3 = open(fc, "x")
        # file starts with the lengths of the characters
        f3.write(lengths)
        # add each differing character from the differences list to the errors file
        for x in differences:
            f3.write("\n")
            f3.write(x)
    # if the files are the same
    else:
        # print that the files are the same
        print("Identical Files")
