#!/usr/bin/python
import csv
import re

filename = 'inputkeywords.csv'
filetowrite = open('keywords.csv', 'w', newline='')

def CleanupKeyword(inputkeyword):
    try: 
        if inputkeyword[:3]=="For": # forla başlayanlar
            inputkeyword=inputkeyword[4:]
        if re.search("(\s\d{1,3}(MP|[+])\S*.*?)",inputkeyword): # 45MP+34MP vesaire kameraları trim
            inputkeyword = re.sub("(\s\d{1,3}(MP|[+])\S*.*?)", "", inputkeyword)
            #if inputkeyword.endswith(' '):
            #    inputkeyword = inputkeyword+"complete"
            #else:
            #    inputkeyword = inputkeyword+" complete"
    except:
        print("hata")
        
    inputkeyword = re.sub("back cover", "battery cover", inputkeyword.lower())   #back cover - battery cover
    inputkeyword = re.sub("[\(\[].*?[\)\]]", "", inputkeyword) # parantez içlerini silme
    inputkeyword = re.sub("  ", " ", inputkeyword) # double space 
    trimlist = ["pulled", "zy", "black", "white", "ref.", "in-cell", "oled", "in cell", "for"]
    keywordwords = inputkeyword.split()
    resultwords  = [word for word in keywordwords if word.lower() not in trimlist]
    inputkeyword = ' '.join(resultwords)

    return inputkeyword

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    writer = csv.writer(filetowrite)
    for row in datareader:
        inputkeyword=""
        try:
            inputkeyword=CleanupKeyword(row[0])
        except:
            print("Sikinti")
        datatowrite=[inputkeyword]
        writer.writerow(datatowrite)
        