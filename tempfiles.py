import os
import shutil
import tempfile

def main():
    tmp_Folder='C:\\Windows\\Temp\\'
    for root, dirs, files in os.walk(tmp_Folder, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except:
                pass
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except:
                pass
    tmp_Folder_Appdata=(tempfile.gettempdir())+'\\'
    for root, dirs, files in os.walk(tmp_Folder_Appdata, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except:
                pass
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except:
                pass
    
