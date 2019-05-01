import os
import shutil
def main(cky,hist,tf):
    appdata=os.getenv('APPDATA')
    path=appdata[0]+':\\Users\\'
    for root,dirs,files in os.walk(path,topdown=False):
        for name in dirs:
            if name=='Microsoft':
                rem((os.path.join(root,name)),cky,hist,tf)

def rem(path,cky,hist,tf):
    for root,dirs,files in os.walk(path,topdown=False):
        for name in dirs:
            if(cky==1):
                if name=='Cookies':
                    try:
                        shutil.rmtree(os.path.join (root,name))
                    except:
                        pass
            if(hist==1):
                if name=='History':
                    try:
                        shutil.rmtree(os.path.join(root,name))
                    except:
                        pass
                
        if tf==1:
            for name in dirs:
                if name=='Temporary Internet Files':
                    try:
                        shutil.rmtree(os.path.join(root,name))
                    except:
                        pass
                

