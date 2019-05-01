import os

def main():
    userhome=os.path.expanduser('~')
    desktop=userhome+'\\Desktop\\'
    desk_folder=desktop+'Desktop Contents\\'
    if not os.path.exists(desk_folder):
        os.makedirs(desk_folder)
    for file in os.listdir(desktop):
        if file!='Desktop Contents':
            os.rename(desktop+file,desk_folder+file)            
    

