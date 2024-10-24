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

