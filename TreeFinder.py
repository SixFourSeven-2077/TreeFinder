#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datetime, os
from colorama import init, Fore, Back, Style
import glob
from pathlib import Path
import fnmatch
os.system("mode con: cols=80 lines=20")
init()
def banner():
    os.system('cls')
    print(Fore.GREEN + Style.BRIGHT + "  ______               _______           __  \n"+
" /_  __/_______  ___  / ____(_)___  ____/ /__  _____\n"+
"  / / / ___/ _ \/ _ \/ /_  / / __ \/ __  / _ \/ ___/\n"+
" / / / /  /  __/  __/ __/ / / / / / /_/ /  __/ /  \n"+
"/_/ /_/   \___/\___/_/   /_/_/ /_/\__,_/\___/_/     "+ Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + " Recursive string searcher\n" + Style.RESET_ALL)

def displayInfo():
    banner()
    print("Searching for '{}' in '{}' files".format(Fore.CYAN + Style.BRIGHT + toFind + Style.RESET_ALL,Fore.CYAN + Style.BRIGHT + ext + Style.RESET_ALL))
    print("{}/{} file(s) analysed ({} remaining)".format(Fore.CYAN + Style.BRIGHT + str(scannedFilesNb),str(nb) + Style.RESET_ALL, nb-scannedFilesNb))
    print("Lines scanned : {}".format(Fore.CYAN + Style.BRIGHT + str(scannedLines) + Style.RESET_ALL))
    print("Strings found : {} in {} file(s)".format(Fore.GREEN + Style.BRIGHT + str(foundNb) + Style.RESET_ALL, Fore.GREEN + Style.BRIGHT + str(filesFoundNb) + Style.RESET_ALL ))
    print("Report name : {}".format(Fore.YELLOW + Style.BRIGHT + name + Style.RESET_ALL))

if __name__ == '__main__':
    while True:
        banner()
        print("Folder to scan : [default : current directory]")
        pathToScan = input("> ")
        print("Files to scan (use wildcards) : [default : * (all)]")
        ext = input("> ")
        if ext == "":
            ext = "*"
        print("String to find (use wildcards) :")
        toFind = input("> ")
        banner()
        print("Mapping directories...")

        current_dir = Path(__file__).parent
        if pathToScan != "":
            current_dir = pathToScan
        path = "{}\\**\\{}".format(current_dir, ext)
        files = glob.glob(path,recursive=True)
        nb = 0
        scannedFilesNb = 0
        filesFoundNb = 0
        filesToScan = []
        for file in files:
            if os.path.isfile(file) and 'TreeFinderReport_' not in file:
                nb += 1
                filesToScan.append(file)

        dateChar = datetime.datetime.now().strftime('%d.%m.%Y_%H-%M-%S')
        name = "TreeFinderReport_{}.txt".format(dateChar)
        with open(name, 'w') as g:
            g.write("== Search report for the string '{}' in '{}' files ==\n\n".format(toFind, ext))
        g.close()
        findlist = []
        files = filesToScan
        foundNb = 0
        scannedLines = 0
        for file in files:
            displayInfo()
            print("File : {}".format(Fore.YELLOW + Style.BRIGHT + file + Style.RESET_ALL))
            print("\nScan in progress...")
            index = 0
            found = False
            with open(file, encoding='utf-8', errors='ignore') as f:
                datafile = f.readlines()
                for line in datafile:
                    index += 1
                    scannedLines += 1
                    if fnmatch.fnmatch(line.lower(), "*"+toFind.lower()+"*"):
                        foundNb += 1
                        found = True
                        with open(name, 'a') as h:
                            try:
                                h.write("{}, LINE {}\n==> {}\n".format(file, index, line))
                            except:
                                h.write("== This line is not printable\n")
                        h.close()
            if found:
                filesFoundNb += 1
            scannedFilesNb += 1
            f.close()

        if findlist is None:
            print("No matching string.")
        displayInfo()

        if not files:
            print(Fore.RED + Style.BRIGHT + "'{}' files not found".format(Fore.CYAN + ext + Fore.RED))
        else:
            print(Fore.YELLOW + Style.BRIGHT)
            print("Done.")
        input()
