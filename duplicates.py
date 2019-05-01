import os 
def main(path):
    file_list={'aaa':True}
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            if name in file_list:
                file_list[name]=True
                os.remove(os.path.join(root, name))
            else:
                file_list[name]=False
    
   
