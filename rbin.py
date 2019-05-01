from ctypes import windll

def main():
    windll.shell32.SHEmptyRecycleBinA(None,None,7)
