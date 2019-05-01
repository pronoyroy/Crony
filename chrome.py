import os
import shutil
def main(cky,hist,tf):
    appdata=os.getenv('APPDATA')
    path=appdata[0]+':\\Users\\'
    for root,dirs,files in os.walk(path,topdown=False):
        for name in dirs:
            if name=='Chrome':
                rem((os.path.join(root,name)),cky,hist,tf)

def rem(path,cky,hist,tf):
    for root,dirs,files in os.walk(path,topdown=False):
        for name in files:
            if(cky==1):
                if name=='Cookies':
                    try:
                        os.remove(os.path.join (root,name))
                    except:
                        pass
            if(hist==1):
                if name=='History':
                    try:
                        os.remove(os.path.join(root,name))
                    except:
                        pass
                if name=='History Provider Cache':
                    try:
                        os.remove(os.path.join(root,name))
                    except:
                        pass
                if name=='History-journal':
                    try:
                        os.remove(os.path.join(root,name))
                    except:
                        pass
                if name=='Last Tabs':
                    try:
                        os.remove(os.path.join(root,name))
                    except:
                        pass
                if name=='Last Session':
                    try:
                        os.remove(os.path.join(root,name))
                    except:
                        pass
                if name=='Visited Links':
                    try:
                        os.remove(os.path.join(root,name))
                    except:
                        pass
                if name=='SyncData.sqlite3':
                    try:
                        os.remove(os.path.join(root,name))
                    except:
                        pass
        if tf==1:
            for name in dirs:
                if name=='Cache':
                    try:
                        shutil.rmtree(os.path.join(root,name))
                    except:
                        pass
                if name=='Local Storage':
                    try:
                        shutil.rmtree(os.path.join(root,name))
                    except:
                        pass
             



