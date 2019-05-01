import psutil

def main():
    for process in psutil.process_iter():
        try:
            pname=process.name()
            if (pname=='firefox.exe' or pname=='vlc.exe'   or
                pname=='chrome.exe'  or pname=='IDMan.exe' or
                pname=='GoogleCrashHandler64.exe' or
                pname=='googledrivesync.exe' or
                pname=='wmplayer.exe'or pname=='Picasa3.exe' or
                pname=='calc.exe'):

                process.kill()
                
        except :
            pass
      


