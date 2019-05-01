import os
import shutil
def main(cky,hist,tf):
    appdata=os.getenv('APPDATA')
    path=appdata[0]+':\\Users\\'
    for root,dirs,files in os.walk(path,topdown=False):
        for name in dirs:
            if name=='Firefox':
                rem((os.path.join(root,name)),cky,hist,tf)

def rem(path,cky,hist,tf):
    for root,dirs,files in os.walk(path,topdown=False):
        for name in files:
            if(cky==1):
                if name=='cookies.sqlite':
                    try:
                        os.remove(os.path.join (root,name))
                    except:
                        pass
            if(hist==1):
                if name=='places.sqlite':
                    try:
                        os.remove(os.path.join(root,name))
                    except:
                        pass
                
        if tf==1:
            for name in dirs:
                if name=='cache':
                    try:
                        shutil.rmtree(os.path.join(root,name))
                    except:
                        pass
                if name=='cache2':
                    try:
                        shutil.rmtree(os.path.join(root,name))
                    except:
                        pass
             






        
