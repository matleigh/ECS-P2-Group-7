#Tamar Shuster

import pandas as pd #xxlrd xlrd3 try to install if pandas isn't working
xl = pd.read_excel("P2M012_G7.xlsx")
# sets two global variables (bins and chars) to the values set in
# ^the excel file
bins = list(xl["Bins"]) #sets binary numbers to list as bins
chars = list(xl["Chars"]) #sets characters to list as chars

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