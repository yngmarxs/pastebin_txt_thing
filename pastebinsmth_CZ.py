import os
import numpy as np
import sys
import requests

FileContentArray2 = []                                   #Uvedení listu

FilePath = r"C:\Users\PC\Desktop\ToDo_List.txt"          #definice cesty souboru
FileContent = open(FilePath, "r")                        #Otevření souboru
FileContentArray = FileContent.read().split("\n")        #Rozdělení souboru na řádky

PastebinURL = r"https://pastebin.com/raw/xxxxxxxx"       #cesta stránky
PastebinResponse = requests.get(PastebinURL)             #zpracování požadavku 1
PastebinContent = PastebinResponse.text                  #zpracování požadavku 2
PastebinContentArray = PastebinContent.split("\r\n")     #Rozdělení souboru na řádky
print("DEBUG1",PastebinContentArray)
print("DEBUG2",len(FileContentArray))
#BORDEL ALE NĚJAK TO FUNGUJE
for PastebinRadek in PastebinContentArray:
    for radek in FileContentArray:
        if radek == PastebinRadek:
            pass
        else:
            FileContentArray.append(PastebinRadek)
            break

FileContentArray2 = str('\n'.join(FileContentArray))    #spojení listu
f=open(r"C:\Users\PC\Desktop\ToDo_List.txt", "w+")      #otevření souboru
f.write(FileContentArray2)                              #uložení do souboru
f.close()                                               #uložení souboru
