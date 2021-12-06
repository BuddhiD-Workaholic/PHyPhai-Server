import os
import urllib.request
import subprocess as sp
import ctypes, sys
from sys import platform
from zipfile import ZipFile

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def install_PHP():    
    try:
        sp.check_call(['php', '-v'])
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
                    newpath = r'C:\PHP' 
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    
                    fullfilename = os.path.join('C:\PHP', 'PHP 8.1.0.zip')
                    urllib.request.urlretrieve("https://windows.php.net/downloads/releases/php-8.1.0-Win32-vs16-x64.zip", fullfilename)

                    #File extraction 
                    zf = ZipFile('C:\PHP\PHP 8.1.0.zip', 'r')
                    zf.extractall('C:\PHP')
                    zf.close()
                        
                    #System Path change
                    os.system('setx /M path "%path%;C:\PHP"')            
                else:
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)   
