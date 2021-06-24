#!/usr/bin/env python3
import glob
import easygui
from easygui import msgbox

wordList = []
replaceList = []
header = ""

def ReadConfig(fileName):
    with open(fileName) as myFile:
        text = myFile.read()
    result = text.split(";")
    words = result[0].split("{")[1].split("}")[0].split(",")
    global header
    header = result[1].split("{")[1].split("}")[0]
    for word in words:
        currentWord = word.split(":")
        if currentWord[0].strip() != "null":
            wordList.append(currentWord[0].strip())
            replaceList.append(currentWord[1].strip())

def ReplaceWords(fileName):
    f = open(fileName, 'r')
    filedata = f.read()
    f.close()

    for i in range(len(wordList)):
        newdata = filedata.replace(wordList[i], replaceList[i])

    f = open(fileName, 'w')
    f.write(newdata)
    f.close()


def AddHeader(fileName):

    f = open(fileName, 'r')
    filedata = f.read()
    f.close()

    f = open(fileName.replace(".nc", ".gcode"), 'w')
    f.write(";Header Start"+header+";Header End\n"+filedata)
    f.close()


def FindFile():
    #if len(glob.glob('./*.nc'))>1:
    #    print("Error")
    #for file in glob.glob('./*.nc'):
    #    return file.split('\\')[1]
    return easygui.fileopenbox()

if __name__ == "__main__":
    fileName = FindFile()
    ReadConfig("config.txt")
    AddHeader(fileName)
    ReplaceWords(fileName.replace(".nc", ".gcode"))
    msgbox("Gcode Is Generated", "Success!")
