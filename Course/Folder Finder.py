import os
import shutil

folder_copy = input("Enter a folder name to copy: ")
folder_location = input("Enter a location to find "+folder_copy+""" (otherwise leave blank, but it may take a while and/or 
                            find a different folder with the same name): """)
if folder_location == "":
    folder_location = "C:\\"
folder_paste = input("""Enter a location to paste the folder, 
For Eg. C:\\\\Users\\\\Siva (leave blank to paste it in the desktop): """)
if folder_paste == "":
    folder_paste = "C:\\Users\\Siva\\Desktop"

num = 1
folderFound = False
for folderName, subFolders, fileNames in os.walk(folder_location):
    #print("FOLDER: "+folderName)
    #print("SUB: "+str(subFolders))
    #print("FILES: "+str(fileNames))
    print("Searched "+str(num)+" files")
    num += 1
    for sub_folder in subFolders:
        if sub_folder == folder_copy:
            print("Folder found.")
            print("Copying...")
            shutil.copytree(folderName+"\\"+sub_folder, folder_paste+"\\"+folder_copy+"(copy)")
            folderFound = True
            print("Copied.")
            break
    if folderFound:
        break
if not folderFound:
    print("Folder not found.")
