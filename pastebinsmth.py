import os
import numpy as np
import sys
import requests

FileContentArray2 = []                                      #init list

FilePath = r"C:\Users\PC\Desktop\ToDo_List.txt"             #define path
FileContent = open(FilePath, "r")                           #open file in path
FileContentArray = FileContent.read().split("\n")           #split to array

PastebinURL = r"https://pastebin.com/raw/xxxxxxxx"          #define site
PastebinResponse = requests.get(PastebinURL)                #request from site
PastebinContent = PastebinResponse.text                     #text from request
PastebinContentArray = PastebinContent.split("\r\n")        #split to array
print("DEBUG1",PastebinContentArray)
print("DEBUG2",len(FileContentArray))
#I DONT KNOW WHAT THIS IS OR HOW IT WORKS, AND IM HAPPY THAT IT WORKS
for PastebinLine in PastebinContentArray:
    for line in FileContentArray:
        if line == PastebinLine:
            pass
        else:
            FileContentArray.append(PastebinLine)
            break


FileContentArray2 = str('\n'.join(FileContentArray))       #join array
f=open(r"C:\Users\PC\Desktop\ToDo_List.txt", "w+")         #open file in path
f.write(FileContentArray2)                                 #write to file
f.close()                                                  #save file
