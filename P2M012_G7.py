#Tamar Shuster
#goal is to read an Excel file and find binary values and characters using dictionary and lists
import pandas as pd #xxlrd xlrd3 try to install if pandas isn't working
xl = pd.read_excel("P2M012_G7.xlsx", dtype=str)
# sets two global variables (bins and chars) to the values set in
# ^the Excel file
bins = list(xl["Bin"]) #sets binary numbers to list as bins
chars = list(xl["Char"]) #sets characters to list as chars

compareDict = {} #empty dictionary: compares pairs from bins and chars lists

chars2 = [] # empty list: initializing the end list

for key in bins:
    for string in chars:
        if string == "\\n": # checks if the value in chars is \\n
            string = "\n"  #sets the value in chars as \n if its \\n
        elif string == "<space>": # same as previous applies with space
            string = " "
        compareDict[key]= string # sets pairs from both lists as loop iterates
        chars2.append(string) # makes new lists without \\n

        # below removes \\n and <space> from the char list
        if string == "\n":
            chars.remove('\\n')
        elif string == " ":
            chars.remove('<space>')
        else:
            chars.remove(string)
        break


# Yavuz Yildiz
# Encoding the text file
# Text to Binary
def encode(fn: str):
    bin_output = "" # Starts with empty string
    with open(fn, 'r') as file: # Is used to read the file
        text = file.read()

    #Loops through each character in the file
    for char in text:
        #Finding the index of the character in the global characters
        if char in chars2:
            index = chars2.index(char)
            #Using index to find matching binary code
            bin_output += str(bins[index])
    total_bits = len(bin_output) #Total number of bits used
    #Write to BinOutput.txt
    with open('BinOutput.txt', 'w') as file: #Is used to write the file
        file.write(f"{total_bits}.{bin_output}")


# Hang Yu Chen
# Decoding the binary
# Binary to text
def decode(fn="BinOutput.txt"):
    # Open the file and read the binary data
    fa = open(fn)
    data = fa.read()

    # Remove any "D." markers from the data
    period = data.index(".")
    cleaned_data = data[period+1:]

    decoded_text = ""  # Initialize an empty string to store decoded characters
    i = 0
    # Loop through the binary data, decoding each binary code
    while i < len(cleaned_data):
        # Determine the binary code length based on the first bit
        if cleaned_data[i] == '1':  # Assume 1 indicates a 7-bit character
            binary_code = cleaned_data[i:(i + 7)]
            i += 7
        else:  # Assume otherwise it's a 6-bit character
            binary_code = cleaned_data[i:(i + 6)]
            i += 6

        # Use compareDict to find the corresponding character
        decoded_text += compareDict[binary_code]

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
                # if the characters are different, create a string variable of
                #   the format "N: C1: C2"
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


encode("test.txt")
decode()
same("test.txt")


