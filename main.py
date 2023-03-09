#!/bin/python
import os
import sys

def getFind(cmakeList, find, i = 0):
    reezult = ''
    i = cmakeList.find(find, i)
    if i == -1:
        return -1, ''
    i += len(find)
    for i in range(i, len(cmakeList)):
        ch = cmakeList[i]
        if(ch != ' ' and ch != '\n' and ch != '\t'):
            for i in range(i, len(cmakeList)):
                ch = cmakeList[i]
                if (ch == ' ' or ch == '\n' or ch == '\t' or ch == ')'):
                    break
                reezult += ch
            break
    return i, reezult

def getBool(default = True):
    match str(input()):
        case "":
            return default
        case "y":
            return True
        case "n":
            return False

def getInstallCommand(default):
    if len(sys.argv) == 1:
        return default
    else:
        return sys.argv[1]

def find1Option(cmakeList, find):
    cursor = 0
    reezults = []
    reezult = ''
    while cursor != -1:
        if cursor != 0:
            reezults.append(reezult)
        cursor, reezult = getFind(cmakeList, find, cursor)

    return reezults

def getLibsInCmake(cmakeListDir):
    cmakeList = open(cmakeListDir + '/CMakeLists.txt', 'r').read()

    libs = []
    libs += find1Option(cmakeList, 'find_package(')
    files = find1Option(cmakeList, 'add_subdirectory(')
    for file in files:
        libs += getLibsInCmake(cmakeListDir + file)

    return libs

libs = list(set(getLibsInCmake('./')))
commands = []
for lib in libs:
    commands.append(getInstallCommand('vcpkg install ') + lib)

print('start? ', commands, '[Y/n]')
if (getBool()):
    for command in commands:
        os.system(command)
