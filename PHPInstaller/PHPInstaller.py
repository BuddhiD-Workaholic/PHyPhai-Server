import os
import urllib.request
import subprocess as sp
import ctypes, sys
import time
import ssl
from sys import platform
from zipfile import ZipFile


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def install_PHP():
    try:
        X=sp.check_call(['php', '-v'])
        print("It seems PHP is already installed to your system!");
    except:
        if platform == "linux" or platform == "linux2":
            KillP = 'sudo apt install php'
            os.system(KillP)
        elif platform == "darwin":
            KillP = 'curl -s http://php-osx.liip.ch/install.sh | bash -s 7.3'
            os.system(KillP)
        elif platform == "win32":
                if is_admin():
                    ssl._create_default_https_context = ssl._create_unverified_context 
                    newpath = r'C:\PHP' 
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    else: 
                        print("This device already contain a PHP folder on this location "+newpath+"\n Delete that file to proceed with the instalaltion!")
                        time.sleep(40)
                        sys.exit()    
                    try:
                        print("Downloading PHP...")   
                        fullfilename = os.path.join('C:\PHP', 'PHP 8.1.0.zip')
                        if platform.architecture()[0] == "32bit":
                            urllib.request.urlretrieve("https://windows.php.net/downloads/releases/php-8.1.0-Win32-vs16-x86.zip", fullfilename)
                        elif platform.architecture()[0] == "64bit":
                            urllib.request.urlretrieve("https://windows.php.net/downloads/releases/php-8.1.0-Win32-vs16-x64.zip", fullfilename)
                        else: 
                            print("There's been an error, Download PHP manually!")
                            sys.exit()
                        #File extraction 
                        zf = ZipFile('C:\PHP\PHP 8.1.0.zip', 'r')
                        zf.extractall('C:\PHP')
                        zf.close()
                        print("PHP Downloaded!")
                    except:
                        print(sys.exc_info()[0])
                        print("There's been an error!, The Web resource folder is corrupted or wrong WEB resource URL is added! \n")
                                                 
                    #System Path change
                    os.system('setx /M path "%path%;C:\PHP"')
                    print("PHP is installed!")
                    time.sleep(20)            
                else:
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)   

install_PHP()