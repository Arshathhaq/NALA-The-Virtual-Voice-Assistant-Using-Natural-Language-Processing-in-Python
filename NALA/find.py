import sys 
import os 
import string
import glob
fileToSearch = '' 
Folder = None


print ("Please enter your starting directory: ")
rootFldr = input() 
print ("Please enter the file to search for including the extension: ")
fileToSearch = input()

for root, dirs, files in os.walk(rootFldr): 
    for fCntr in files: 
            if fCntr == fileToSearch: 
                Folder = root 
                print (Folder) 
os.listdir(Folder)            
g= glob.glob("*.exe")
for i in g:
        stem = os.path.basename(i)
        print(stem)
        stem = os.path.splitext(stem)
        print("\n",stem)
        if stem[0] == fileToSearch:
            print(i)
            os.startfile(i)

                    
                